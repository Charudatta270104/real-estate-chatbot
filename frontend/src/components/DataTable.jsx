import React from "react";

const DataTable = ({ data }) =>
  data.length ? (
    <div className="table-box">
      <h3>Data Table:</h3>
      <div className="table-scroll">
        <table>
          <thead>
            <tr>
              {Object.keys(data[0]).map((key) => (
                <th key={key}>{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, idx) => (
              <tr key={idx}>
                {Object.values(row).map((val, i) => (
                  <td key={i}>{val}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  ) : null;

export default DataTable;
