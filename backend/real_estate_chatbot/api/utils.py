# import pandas as pd
# import os

# # Path to your sample Excel data file
# DATA_PATH = os.path.join(os.path.dirname(__file__), 'sample_data', 'real_estate_data.xlsx')

# def load_data():
#     try:
#         df = pd.read_excel(DATA_PATH)
#         return df
#     except Exception as e:
#         print("Error loading Excel file:", e)
#         return pd.DataFrame()

# def analyze_area(query):
#     df = load_data()
#     if df.empty:
#         return "No data found.", [], []

#     query_lower = query.lower()

#     # Compare demand trends
#     if "compare" in query_lower and "demand" in query_lower:
#         try:
#             # Extract areas from the query
#             parts = query_lower.replace("compare", "").replace("demand trends", "").strip()
#             areas = [area.strip() for area in parts.split("and")]
#             filtered = df[df['area'].str.lower().isin([a.lower() for a in areas])]

#             if filtered.empty:
#                 return "No data found for the specified areas.", [], []

#             chart_data = (
#                 filtered.groupby(['area', 'year'])['demand']
#                 .mean().reset_index()
#                 .to_dict(orient="records")
#             )

#             summary = f"Compared demand trends for {', '.join(areas)}."  # Mocked
#             return summary, chart_data, filtered.to_dict(orient="records")
#         except:
#             return "Error processing comparison query.", [], []

#     # Price growth or single area analysis
#     elif "price growth" in query_lower or "analyze" in query_lower or "show" in query_lower:
#         try:
#             area = ""
#             if "for" in query_lower:
#                 area = query_lower.split("for")[-1].strip().replace("over last 3 years", "")
#             elif "analyze" in query_lower:
#                 area = query_lower.replace("analyze", "").strip()
#             else:
#                 return "Please specify a valid area.", [], []

#             filtered = df[df['area'].str.lower() == area.lower()]
#             if filtered.empty:
#                 return f"No data found for {area}.", [], []

#             chart_data = (
#                 filtered.groupby('year')['price']
#                 .mean().reset_index()
#                 .to_dict(orient="records")
#             )

#             summary = f"{area.title()} shows a steady growth in price."  # Mocked
#             return summary, chart_data, filtered.to_dict(orient="records")
#         except:
#             return "Error processing area analysis query.", [], []

#     return "Query not understood. Try asking about price or demand trends.", [], []


import pandas as pd
import os

# Path to your Excel data file
DATA_PATH = os.path.join(os.path.dirname(__file__), 'sample_data', 'real_estate_data.xlsx')

def load_data():
    try:
        df = pd.read_excel(DATA_PATH)
        print("\n[DEBUG] Excel data loaded successfully.")
        print("[DEBUG] Columns:", df.columns.tolist())
        print("[DEBUG] First 5 rows:\n", df.head())

        # 🔁 Normalize the column used for filtering (this was 'area' originally)
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

    # 🟡 Compare demand trends
    if "compare" in query_lower and "demand" in query_lower:
        try:
            parts = query_lower.replace("compare", "").replace("demand trends", "").strip()
            areas = [area.strip().lower() for area in parts.split("and")]
            print("[DEBUG] Parsed areas for comparison:", areas)

            filtered = df[df['final location'].isin(areas)]
            print("[DEBUG] Filtered rows:\n", filtered)

            if filtered.empty:
                return "No data found for the specified areas.", [], []

            # Example: average demand per area per year
            chart_data = (
                filtered.groupby(['final location', 'year'])['flat total']
                .mean().reset_index()
                .rename(columns={"final location": "area"})
                .to_dict(orient="records")
            )

            summary = f"Compared demand trends for {', '.join(areas)}."
            return summary, chart_data, filtered.to_dict(orient="records")
        except Exception as e:
            print("[ERROR] Error in compare demand block:", e)
            return "Error processing comparison query.", [], []

    # 🟢 Price growth or area-specific analysis
    elif "price growth" in query_lower or "analyze" in query_lower or "show" in query_lower:
        try:
            area = ""
            if "for" in query_lower:
                area = query_lower.split("for")[-1].strip().replace("over last 3 years", "")
            elif "analyze" in query_lower:
                area = query_lower.replace("analyze", "").strip()

            area = area.lower().strip()
            print("[DEBUG] Parsed area for single analysis:", area)

            filtered = df[df['final location'] == area]
            print("[DEBUG] Filtered rows:\n", filtered)

            if filtered.empty:
                return f"No data found for {area}.", [], []

            # Example: price per year (you can change column to match yours)
            chart_data = (
                filtered.groupby('year')['flat - weighted average rate']
                .mean().reset_index()
                .to_dict(orient="records")
            )

            summary = f"{area.title()} shows a steady growth in price."
            return summary, chart_data, filtered.to_dict(orient="records")
        except Exception as e:
            print("[ERROR] Error in single area analysis block:", e)
            return "Error processing area analysis query.", [], []

    print("[DEBUG] Query did not match any known pattern.")
    return "Query not understood. Try asking about price or demand trends.", [], []
