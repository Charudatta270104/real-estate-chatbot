import pandas as pd
import os
import re

# Path to your Excel data file
DATA_PATH = os.path.join(os.path.dirname(__file__), 'sample_data', 'real_estate_data.xlsx')

def load_data():
    try:
        df = pd.read_excel(DATA_PATH)
        print("\n[DEBUG] Excel data loaded successfully.")
        print("[DEBUG] Columns:", df.columns.tolist())
        print("[DEBUG] First 5 rows:\n", df.head())

        df['final location'] = df['final location'].astype(str).str.strip().str.lower()
        return df
    except Exception as e:
        print("[ERROR] Failed to load Excel file:", e)
        return pd.DataFrame()

def analyze_area(query):
    print("\n[DEBUG] Received query:", query)
    df = load_data()
    if df.empty:
        print("[DEBUG] DataFrame is empty after loading.")
        return "No data found.", [], []

    query_lower = query.lower()

    #  Compare demand trends
    if "compare" in query_lower and "demand" in query_lower:
        try:
            parts = query_lower.replace("compare", "").replace("demand trends", "").strip()
            areas = [area.strip().lower() for area in parts.split("and")]
            print("[DEBUG] Parsed areas for comparison:", areas)

            filtered = df[df['final location'].isin(areas)]
            print("[DEBUG] Filtered rows:\n", filtered)

            if filtered.empty:
                return "No data found for the specified areas.", [], []

            chart_data = (
                filtered.groupby(['final location', 'year'])['flat total']
                .sum().reset_index()
                .rename(columns={'final location': 'area'})
                .to_dict(orient='records')
            )

            summary = f"Compared demand trends for {', '.join([a.title() for a in areas])}."
            return summary, chart_data, filtered.to_dict(orient='records')
        except Exception as e:
            print("[ERROR] Error in compare demand block:", e)
            return "Error processing comparison query.", [], []

    #  Single area queries: analyze, price growth, or show demand
    elif any(kw in query_lower for kw in ["analyze", "price growth", "show", "demand for", "analysis of"]):
        try:
            # Extract area from query
            area_match = re.search(r"(analyze|price growth for|show|demand for|analysis of)\s+([a-zA-Z\s]+)", query_lower)
            if area_match:
                area = area_match.group(2).replace("over last 3 years", "").strip().lower()
            else:
                return "Could not detect area from query.", [], []

            print("[DEBUG] Parsed area for single analysis:", area)

            filtered = df[df['final location'] == area]
            print("[DEBUG] Filtered rows:\n", filtered)

            if filtered.empty:
                return f"No data found for {area}.", [], []

            # Group demand over years and include area for chart
            grouped = (
                filtered.groupby('year')['flat total']
                .sum().reset_index()
            )
            grouped['area'] = area.title()
            chart_data = grouped.to_dict(orient='records')

            summary = f"Showing analysis for {area.title()}."
            return summary, chart_data, filtered.to_dict(orient='records')
        except Exception as e:
            print("[ERROR] Error in single area analysis block:", e)
            return "Error processing area analysis query.", [], []

    print("[DEBUG] Query did not match any known pattern.")
    return "Query not understood. Try asking about price or demand trends.", [], []
