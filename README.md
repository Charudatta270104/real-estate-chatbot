# Real Estate Analysis Chatbot

## Overview

This project is a web-based chatbot that helps users analyze real estate data. It uses React for the frontend and Django for the backend. Users can input queries related to real estate areas (e.g., "Analyze Wakad", "Compare demand trends for Akurdi and Wakad"), and the system will respond with:

- A short natural language summary of the data.
- A chart (price trend or demand comparison).
- A filtered data table based on the query.

This project is designed to handle real estate data provided in an Excel file, which is parsed and analyzed in the backend using Python.

## Features

- **Real Estate Analysis**: Allows users to analyze trends, price growth, and demand comparisons in different areas.
- **Chart Visualizations**: Displays demand trends, price growth, and comparison charts using libraries like `Chart.js` or `Recharts`.
- **Data Table**: Displays the filtered data based on the user query.
- **Responsive Design**: The interface is mobile and tablet-friendly, ensuring usability on all devices.

## Technologies Used

### Frontend:

- React
- React Hooks
- Axios (for making API requests)
- Recharts (for chart visualization)
- CSS (for styling)

### Backend:

- Django (for API endpoints)
- Python (for data processing)
- Pandas (for Excel file processing)
- `openpyxl` (for reading Excel files)
- REST framework (for API integration)

### Optional:

- OpenAI API (for generating real LLM summaries)

## Installation Instructions

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/real-estate-chatbot.git
cd real-estate-chatbot
```

### Step 2: Backend Setup (Django)

```bash
To set up the backend, follow these steps:

1. Navigate to the backend directory: cd backend

2.Create and activate a virtual environment (recommended):
	i)for linux/macOS: python -m venv venv
	ii)for windows : python -m venv venv
3.Install the required dependencies:pip install -r requirements.txt

4.Apply database migrations:python manage.py migrate

5. Start the Django server: python manage.py runserver
```

### Step 3: Frontend Setup (React)

```bash
1. Navigate to the frontend directory:cd frontend
2.Install the required dependencies:npm install
3. Start the React development server:npm start

The frontend should now be running at http://localhost:3000.
```

### Step 4: Upload Excel Data (Optional)

```bash
For testing purposes, you can upload an Excel file containing the real estate data through the backend. The file should include columns such as year, area, price, demand, size, etc.

The system will parse the file and make the data available for analysis.

```

### How to Use the Chatbot:

```bash
	1. Open the frontend in a browser (http://localhost:3000).
	2.Enter a query in the chat input box. Sample queries:

		"Analyze Wakad"

		"Compare demand trends for Akurdi and Wakad"

		"Show price growth for Akurdi over last 3 years"
	3. The chatbot will respond with
		"Analyze Wakad": Analyzes all data related to Wakad.

		"Compare demand trends for Akurdi and Wakad": Compares the demand trends between Akurdi and Wakad over the years.

		"Show price growth for Akurdi over last 3 years": Displays the price growth for Akurdi from the last 3 years.

```

### Structure

```bash
real-estate-chatbot/
├── backend/
│   ├── real_estate_analysis/
│   ├── manage.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── ...
│   ├── package.json
│   └── ...
├── .gitignore
└── README.md

```
