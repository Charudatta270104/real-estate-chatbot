# Real Estate Analysis Chatbot

## Overview

This project is a **web-based chatbot** that helps users analyze real estate data. It uses **React** for the frontend and **Django** for the backend. Users can input queries related to real estate areas (e.g., "Analyze Wakad", "Compare demand trends for Akurdi and Wakad"), and the system will respond with:

- A short natural language summary of the data.
- A chart (price trend or demand comparison).
- A filtered data table based on the query.

The backend processes real estate data provided in an Excel file, which is parsed and analyzed using Python.

---

## Features

- **Real Estate Analysis**: Analyze trends, price growth, and demand comparisons for different areas.
- **Chart Visualizations**: Demand trends, price growth, and comparison charts using libraries like `Chart.js` or `Recharts`.
- **Data Table**: Displays filtered data based on user queries.
- **Responsive Design**: Mobile and tablet friendly for usability on all devices.

---

## Technologies Used

### Frontend

- React
- React Hooks
- Axios (for API requests)
- Recharts (for chart visualization)
- CSS (for styling)

### Backend

- Django (API endpoints)
- Python (data processing)
- Pandas (Excel file processing)
- `openpyxl` (reading Excel files)
- Django REST framework (API integration)

### Optional

- OpenAI API (for generating real LLM summaries)

---

## Project Structure

```
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

## Installation Instructions

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/real-estate-chatbot.git
cd real-estate-chatbot
```

---

### Step 2: Backend Setup (Django)

```bash
# Navigate to the backend directory
cd backend

# Create and activate a virtual environment (recommended)
# For Linux/macOS:
python -m venv venv
source venv/bin/activate

# For Windows:
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver
```

---

### Step 3: Frontend Setup (React)

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

The frontend will be available at: `http://localhost:3000`

---

### Step 4: Upload Excel Data (Optional)

You can upload an Excel file containing real estate data through the backend API. The file should include columns like:

- year
- area
- price
- demand
- size
- etc.

The backend will parse this file and prepare the data for analysis.

---

## How to Use the Chatbot

1. Open the frontend in your browser: `http://localhost:3000`
2. Enter queries in the chat input box. Examples:

   - `"Analyze Wakad"`
   - `"Compare demand trends for Akurdi and Wakad"`
   - `"Show price growth for Akurdi over last 3 years"`

3. The chatbot will respond with:

   - For `"Analyze Wakad"`: Analysis of all data related to Wakad.
   - For `"Compare demand trends for Akurdi and Wakad"`: Demand trend comparison over the years.
   - For `"Show price growth for Akurdi over last 3 years"`: Price growth data for Akurdi over the last 3 years.

---

### Price Growth Chart for Wakad

![Price Growth Chart](/frontend/public/images/price_growth_wakad.png)

### Demand Comparison for Akurdi and Wakad

![Demand Comparison Chart](/frontend/public/images/demand_comparison_akurdi_wakad.png)
