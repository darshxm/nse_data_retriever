import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date, timedelta
from retriever import NSEDataRetriever, Broad_Indices, Sectoral_Indices, Thematic_Indices, Strategic_Indices

# Combine all index lists into one
all_indices = Broad_Indices + Sectoral_Indices + Thematic_Indices + Strategic_Indices

st.title("NSE Index Comparison")
st.write("Select two indices and a valid date range for data retrieval. The dates must be in the past and data must be available for the selected period.")

# Dropdowns for selecting two indices
index1 = st.selectbox("Select Index 1", all_indices, index=0)
index2 = st.selectbox("Select Index 2", all_indices, index=1)

# Date inputs with defaults (adjust as needed)
start_date = st.date_input("Start Date", value=date(2023, 1, 1))
end_date = st.date_input("End Date", value=date(2023, 12, 31))

# Validate the date range before proceeding
if start_date > end_date:
    st.error("Error: The Start Date must be before the End Date.")

def retrieve_data_in_chunks(retriever, index, start_dt, end_dt, max_days=365):
    """
    Retrieves data in multiple 365-day chunks to overcome the 12-month limit,
    then combines the chunks into one DataFrame with proper date ordering.
    """
    data_chunks = []
    current_start = start_dt

    while current_start <= end_dt:
        current_end = min(current_start + timedelta(days=max_days - 1), end_dt)
        
        # Format dates as "DD-MM-YYYY" (or whatever your retriever expects)
        from_date_str = current_start.strftime("%d-%m-%Y")
        to_date_str = current_end.strftime("%d-%m-%Y")

        try:
            df_chunk = retriever.get_data(index, from_date_str, to_date_str)
            data_chunks.append(df_chunk)
        except Exception as e:
            st.error(f"Error retrieving data for {index} from {from_date_str} to {to_date_str}: {e}")
            return pd.DataFrame()

        current_start = current_end + timedelta(days=1)

    if not data_chunks:
        return pd.DataFrame()

    # Combine all chunks
    combined_df = pd.concat(data_chunks, ignore_index=True)

    # Ensure 'Date' is recognized as a datetime
    # Adjust the format or remove "format=" if needed, depending on your data source
    combined_df["Date"] = pd.to_datetime(combined_df["Date"], format="%d-%m-%Y", errors="coerce")

    # Drop rows where 'Date' could not be parsed (if any)
    combined_df.dropna(subset=["Date"], inplace=True)

    # Remove duplicates by date
    combined_df.drop_duplicates(subset="Date", inplace=True)

    # Sort by date in ascending order
    combined_df.sort_values(by="Date", ascending=True, inplace=True)

    return combined_df

if st.button("Plot"):
    # Additional check: no future dates allowed
    if start_date > date.today() or end_date > date.today():
        st.error("Error: The selected date range contains future dates. Please select past dates.")
    else:
        retriever = NSEDataRetriever()

        # Retrieve data in chunks for both indices
        df1 = retrieve_data_in_chunks(retriever, index1, start_date, end_date)
        df2 = retrieve_data_in_chunks(retriever, index2, start_date, end_date)

        # Check if data retrieval returned anything
        if df1.empty or df2.empty:
            st.error("No data found for the given parameters. Please try a different date range or index.")
        else:
            # Set the index to 'Date' and ensure ascending index
            df1.set_index("Date", inplace=True)
            df1.sort_index(inplace=True)

            df2.set_index("Date", inplace=True)
            df2.sort_index(inplace=True)

            # Normalize the 'Close' price so that each series starts at 100
            norm_series1 = (df1["Close"] / df1["Close"].iloc[0]) * 100
            norm_series2 = (df2["Close"] / df2["Close"].iloc[0]) * 100

            # Plot the data
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(norm_series1.index, norm_series1, label=index1)
            ax.plot(norm_series2.index, norm_series2, label=index2)
            ax.set_title("Normalized Close Price Comparison")
            ax.set_xlabel("Date")
            ax.set_ylabel("Normalized Price (Base = 100)")
            ax.legend()
            ax.grid(True)

            st.pyplot(fig)
