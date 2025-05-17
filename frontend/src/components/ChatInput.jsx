import React from "react";

const ChatInput = ({ query, setQuery, onSubmit }) => (
  <div className="chat-input">
    <input
      type="text"
      placeholder="Ask something like: 'Compare wakad and aundh demand trends'"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
    />
    <button onClick={onSubmit}>Submit</button>
  </div>
);

export default ChatInput;
