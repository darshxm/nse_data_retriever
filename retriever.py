import requests
import pandas as pd

from constants import Broad_Indices, Sectoral_Indices, Thematic_Indices, Strategic_Indices

class NSEDataRetriever:
    """
    A class to retrieve historical NSE index data.

    Attributes:
        base_url (str): The base URL for the NSE historical indices API.
        session (requests.Session): A requests session with pre-configured headers and cookies.
    """

    def __init__(self):
        self.base_url = "https://www.nseindia.com/api/historical/indicesHistory"
        self.session = requests.Session()
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.nseindia.com/",
        }
        self.session.headers.update(self.headers)

    def _initialize_session(self):
        """
        Initializes the session by visiting the NSE homepage to retrieve required cookies.
        """
        homepage_url = "https://www.nseindia.com"
        self.session.get(homepage_url, timeout=5)

    def get_data(self, index_type, from_date, to_date):
        """
        Retrieve historical data for a given index type and date range.

        Example:
            >>> from nse_data_retriever import NSEDataRetriever
            >>> retriever = NSEDataRetriever()
            >>> df = retriever.get_data("NIFTY 50", "01-01-2023", "10-01-2023")
            >>> print(df.head())

        Args:
            index_type (str): The index type (e.g., 'NIFTY 50'), must be in Broad_Indices, etc.
            from_date (str): Start date in DD-MM-YYYY format.
            to_date (str): End date in DD-MM-YYYY format.

        Returns:
            pd.DataFrame: DataFrame with columns [Index, Open, High, Low, Close, Date].

        Raises:
            ValueError: If index_type is invalid or no data found for the given parameters.
            RequestException: If there's an issue with the HTTP request (network/server).
        """
        # Validate the index_type
        all_indices = Broad_Indices + Sectoral_Indices + Thematic_Indices + Strategic_Indices
        if index_type not in all_indices:
            raise ValueError(
                f"Invalid index_type '{index_type}'. Must be one of the following:\n"
                f"{all_indices}"
            )

        # Initialize session to set cookies
        self._initialize_session()

        params = {
            "indexType": index_type,
            "from": from_date,
            "to": to_date
        }

        response = self.session.get(self.base_url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Extracting the required data
        records = data.get("data", {}).get("indexCloseOnlineRecords", [])

        if not records:
            raise ValueError("No data found for the given parameters.")

        # Convert records to a DataFrame
        df = pd.DataFrame(records)

        # Drop '_id' and 'TIMESTAMP' columns
        df = df.drop(columns=["_id", "TIMESTAMP"])

        # Convert 'EOD_TIMESTAMP' to datetime
        df["EOD_TIMESTAMP"] = pd.to_datetime(df["EOD_TIMESTAMP"], format="%d-%b-%Y")

        # Rename columns
        column_names = {
            'EOD_INDEX_NAME': 'Index',
            'EOD_OPEN_INDEX_VAL': 'Open',
            'EOD_HIGH_INDEX_VAL': 'High',
            'EOD_CLOSE_INDEX_VAL': 'Close',
            'EOD_LOW_INDEX_VAL': 'Low',
            'EOD_TIMESTAMP': 'Date'
        }
        df = df.rename(columns=column_names)

        return df

