import json
import pandas as pd
import pytest
from requests.models import Response
from nse_data_retriever import NSEDataRetriever, Broad_Indices, Sectoral_Indices, Thematic_Indices, Strategic_Indices

# Helper function to create a dummy Response object
def dummy_response(json_data, status_code=200):
    response = Response()
    response.status_code = status_code
    response._content = json.dumps(json_data).encode("utf-8")
    return response

# A dummy session to simulate HTTP GET responses without making actual calls.
class DummySession:
    def __init__(self, response):
        self.response = response
        self.headers = {}
    
    def get(self, url, params=None, timeout=None):
        # For debugging, you could print params if needed.
        return self.response

    def update(self, headers):
        self.headers.update(headers)

def test_get_data_success(monkeypatch):
    """Test that valid parameters return a non-empty DataFrame with a proper Date column."""
    # Create dummy JSON response with valid records.
    dummy_json = {
        "data": {
            "indexCloseOnlineRecords": [
                {
                    "_id": "1",
                    "TIMESTAMP": "dummy",
                    "EOD_INDEX_NAME": "NIFTY 50",
                    "EOD_OPEN_INDEX_VAL": 10000,
                    "EOD_HIGH_INDEX_VAL": 10100,
                    "EOD_LOW_INDEX_VAL": 9900,
                    "EOD_CLOSE_INDEX_VAL": 10050,
                    "EOD_TIMESTAMP": "01-Jan-2023"
                },
                {
                    "_id": "2",
                    "TIMESTAMP": "dummy",
                    "EOD_INDEX_NAME": "NIFTY 50",
                    "EOD_OPEN_INDEX_VAL": 10050,
                    "EOD_HIGH_INDEX_VAL": 10200,
                    "EOD_LOW_INDEX_VAL": 10000,
                    "EOD_CLOSE_INDEX_VAL": 10150,
                    "EOD_TIMESTAMP": "02-Jan-2023"
                }
            ]
        }
    }
    dummy_resp = dummy_response(dummy_json)
    dummy_session = DummySession(dummy_resp)
    
    retriever = NSEDataRetriever()
    # Bypass actual session initialization.
    retriever._initialize_session = lambda: None  
    retriever.session = dummy_session

    df = retriever.get_data("NIFTY 50", "01-01-2023", "02-01-2023")
    assert not df.empty, "The returned DataFrame should not be empty."
    assert "Close" in df.columns, "The DataFrame should have a 'Close' column."
    # Check that the Date column is of datetime type.
    assert pd.api.types.is_datetime64_any_dtype(df["Date"]), "The 'Date' column should be datetime."

def test_get_data_no_records(monkeypatch):
    """Test that when no records are returned, a ValueError is raised."""
    dummy_json = {
        "data": {
            "indexCloseOnlineRecords": []
        }
    }
    dummy_resp = dummy_response(dummy_json)
    dummy_session = DummySession(dummy_resp)

    retriever = NSEDataRetriever()
    retriever._initialize_session = lambda: None  
    retriever.session = dummy_session

    with pytest.raises(ValueError, match="No data found for the given parameters."):
        _ = retriever.get_data("NIFTY 50", "01-01-2023", "02-01-2023")

def test_invalid_index():
    """Test that an invalid index type raises a ValueError."""
    retriever = NSEDataRetriever()
    # This index is not in any of the allowed lists.
    with pytest.raises(ValueError, match="Invalid index_type"):
        _ = retriever.get_data("INVALID INDEX", "01-01-2023", "02-01-2023")
