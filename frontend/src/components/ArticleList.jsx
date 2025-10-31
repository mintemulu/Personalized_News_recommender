import React from "react";

export default function ArticleList({ articles }) {
  return (
    <div>
      {articles.length === 0 ? (
        <p>No recommendations yet.</p>
      ) : (
        articles.map((a, idx) => (
          <div key={idx} className="article">
            <h3>{a.title}</h3>
            <p>{a.description}</p>
            <small><b>{a.source}</b></small><br/>
            <a href={a.url} target="_blank" rel="noreferrer">Read More</a>
          </div>
        ))
      )}
    </div>
  );
}
