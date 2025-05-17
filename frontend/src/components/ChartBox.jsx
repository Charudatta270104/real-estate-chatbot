// import React from "react";
// import {
//   LineChart,
//   Line,
//   XAxis,
//   YAxis,
//   Tooltip,
//   Legend,
//   CartesianGrid,
//   ResponsiveContainer,
// } from "recharts";

// const ChartBox = ({ data }) =>
//   data.length ? (

//     <div className="chart-box">
//         {console.log("Chart Data:", data)}

//       <h3>Chart:</h3>
//       <ResponsiveContainer width="100%" height={300}>
//         <LineChart data={data}>
//           <CartesianGrid strokeDasharray="3 3" />
//           <XAxis dataKey="year" />
//           <YAxis />
//           <Tooltip />
//           <Legend />
//           <Line type="monotone" dataKey="price" stroke="#8884d8" />
//           <Line type="monotone" dataKey="demand" stroke="#82ca9d" />
//         </LineChart>
//       </ResponsiveContainer>
//     </div>
//   ) : null;

// export default ChartBox;

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
  // Log the chart data to inspect its structure
  console.log("Chart Data:", data);

  if (!data || data.length === 0) {
    return <div>No chart data available.</div>;
  }

  // Extract unique areas from the data
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

          {/* Render lines dynamically for each area */}
          {areas.map((area, idx) => {
            // Filter data for the current area
            const areaData = data.filter((entry) => entry.area === area);

            return (
              <Line
                key={area}
                type="monotone"
                dataKey="flat total" // Use 'flat total' as the dataKey for demand
                data={areaData} // Filtered data for the current area
                name={area} // Name the line by area
                stroke={["#8884d8", "#82ca9d", "#ffc658"][idx % 3]} // Different color for each area
                dot={false} // Hide dots for cleaner lines
                isAnimationActive={false} // Disable animation for performance
              />
            );
          })}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ChartBox;
