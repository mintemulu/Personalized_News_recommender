import React, { useState } from "react";

export default function InterestInput({ onSubmit }) {
  const [input, setInput] = useState("");

  const handleSubmit = () => {
    const interests = input.split(",").map(i => i.trim());
    onSubmit(interests);
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input
        type="text"
        placeholder="Enter your interests eg : technology, science"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={handleSubmit}>Recommend</button>
    </div>
  );
}
