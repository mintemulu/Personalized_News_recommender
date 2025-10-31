import React, { useState } from "react";
import InterestInput from "./components/InterestInput";
import ArticleList from "./components/ArticleList";
import "./styles.css";

function App() {
  const [articles, setArticles] = useState([]);

  const handleRecommend = async (interests) => {
    const res = await fetch("http://localhost:8000/api/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(interests),
    });
    const data = await res.json();
    setArticles(data);
  };

  return (
    <div className="app">
      <h1>Personalized News Recommender</h1>
      <InterestInput onSubmit={handleRecommend} />
      <ArticleList articles={articles} />
    </div>
  );
}

export default App;
