import React from "react";

const SummaryBox = ({ summary }) =>
  summary ? (
    <div className="summary-box">
      <h3>Summary:</h3>
      <p>{summary}</p>
    </div>
  ) : null;

export default SummaryBox;
