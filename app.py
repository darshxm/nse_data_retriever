import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
from nse_data_retriever import NSEDataRetriever, Broad_Indices, Sectoral_Indices, Thematic_Indices, Strategic_Indices

# Combine all index lists into one
all_indices = Broad_Indices + Sectoral_Indices + Thematic_Indices + Strategic_Indices

st.title("NSE Index Comparison")
st.write("Select two indices and a valid date range for data retrieval. The dates must be in the past and data must be available for the selected period.")

# Dropdowns for selecting two indices
index1 = st.selectbox("Select Index 1", all_indices, index=0)
index2 = st.selectbox("Select Index 2", all_indices, index=1)

# Date inputs with defaults (adjust as needed)
start_date = st.date_input("Start Date", value=date(2023, 1, 1))
end_date = st.date_input("End Date", value=date(2023, 1, 31))

# Validate the date range before proceeding
if start_date > end_date:
    st.error("Error: The Start Date must be before the End Date.")

if st.button("Plot"):
    # Additional check: no future dates allowed
    if start_date > date.today() or end_date > date.today():
        st.error("Error: The selected date range contains future dates. Please select past dates.")
    else:
        retriever = NSEDataRetriever()
        
        # Format the dates as required ("DD-MM-YYYY")
        from_date_str = start_date.strftime("%d-%m-%Y")
        to_date_str = end_date.strftime("%d-%m-%Y")
        
        try:
            # Retrieve data for both indices
            df1 = retriever.get_data(index1, from_date_str, to_date_str)
            df2 = retriever.get_data(index2, from_date_str, to_date_str)
        except Exception as e:
            st.error(f"An error occurred while retrieving data: {e}")
        else:
            if df1.empty or df2.empty:
                st.error("No data found for the given parameters. Please try a different date range or index.")
            else:
                # Ensure the DataFrames have the 'Date' column as index.
                if "Date" in df1.columns:
                    df1.set_index("Date", inplace=True)
                if "Date" in df2.columns:
                    df2.set_index("Date", inplace=True)
                
                # Normalize the 'Close' price so that each series starts at 100.
                norm_series1 = (df1["Close"] / df1["Close"].iloc[0]) * 100
                norm_series2 = (df2["Close"] / df2["Close"].iloc[0]) * 100
                
                # Create the plot
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.plot(norm_series1.index, norm_series1, label=index1)
                ax.plot(norm_series2.index, norm_series2, label=index2)
                ax.set_title("Normalized Close Price Comparison")
                ax.set_xlabel("Date")
                ax.set_ylabel("Normalized Price (Base = 100)")
                ax.legend()
                ax.grid(True)
                
                st.pyplot(fig)
