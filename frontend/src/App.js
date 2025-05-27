import React, { useState } from "react";
import axios from "axios";
import ChatInput from "./components/ChatInput";
import SummaryBox from "./components/SummaryBox";
import ChartBox from "./components/ChartBox";
import DataTable from "./components/DataTable";
import "./index.css";

const App = () => {
  const [query, setQuery] = useState("");
  const [summary, setSummary] = useState("");
  const [chartData, setChartData] = useState([]);
  const [tableData, setTableData] = useState([]);

  const handleSubmit = async () => {
    if (!query.trim()) return;
    try {
      const response = await axios.post(
        "https://real-estate-chatbot-qna4.onrender.com/api/analyze/",
        {
          query,
        }
      );
      setSummary(response.data.summary);
      setChartData(response.data.chart_data);
      setTableData(response.data.table_data);
    } catch (error) {
      alert("Failed to fetch data");
      console.error(error);
    }
  };

  return (
    <div className="app-container">
      <h1 className="title">🏠 Real Estate Analysis Chatbot</h1>
      <ChatInput query={query} setQuery={setQuery} onSubmit={handleSubmit} />
      <SummaryBox summary={summary} />
      <ChartBox data={chartData} />
      <DataTable data={tableData} />
    </div>
  );
};

export default App;
