import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

const ChartBox = ({ data }) => {
  if (!data || data.length === 0) {
    return <div>No chart data available.</div>;
  }

  const areas = [...new Set(data.map((d) => d.area))];

  return (
    <div className="chart-box">
      <h3>Demand Trend Chart:</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="year" />
          <YAxis />
          <Tooltip />
          <Legend />

          {areas.map((area, idx) => {
            const areaData = data.filter((entry) => entry.area === area);

            return (
              <Line
                key={area}
                type="monotone"
                dataKey="flat total"
                data={areaData}
                name={area}
                stroke={["#8884d8", "#82ca9d", "#ffc658"][idx % 3]}
                dot={false}
                isAnimationActive={false}
              />
            );
          })}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ChartBox;
