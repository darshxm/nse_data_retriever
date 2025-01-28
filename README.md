# NSE Data Retriever

![NSE Data Retriever](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![GitHub Issues](https://img.shields.io/github/issues/your-username/nse-data-retriever)
![GitHub Stars](https://img.shields.io/github/stars/your-username/nse-data-retriever?style=social)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Importing the Library](#importing-the-library)
  - [Retrieving Data](#retrieving-data)
  - [Available Indices](#available-indices)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

**NSE Data Retriever** is a Python library designed to fetch historical data for various National Stock Exchange (NSE) indices in India. Whether you're a data analyst, trader, or enthusiast, this library provides a simple and efficient way to access and analyze NSE index data directly within your Python projects.

## Features

- **Comprehensive Index Coverage**: Retrieve data for a wide range of NSE indices, including Broad, Sectoral, Thematic, and Strategic indices.
- **Easy-to-Use Interface**: Simple class-based API for fetching and handling data.
- **Data in Pandas DataFrame**: Get the retrieved data in a structured Pandas DataFrame for easy manipulation and analysis.
- **Input Validation**: Ensures that only valid index types are used, minimizing errors.
- **Session Management**: Handles HTTP sessions and required cookies automatically.

## Installation

Since the library is not yet published on PyPI, you can install it directly from the GitHub repository.

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/nse-data-retriever.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd nse-data-retriever
   ```

3. **Install Dependencies**

   It's recommended to use a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

   Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   *If `requirements.txt` is not provided, install dependencies manually:*

   ```bash
   pip install requests pandas
   ```

## Usage

### Importing the Library

```python
from nse_data_retriever import NSEDataRetriever, Broad_Indices, Sectoral_Indices, Thematic_Indices, Strategic_Indices
```

### Retrieving Data

Instantiate the `NSEDataRetriever` class and use the `get_data` method to fetch historical data.

```python
retriever = NSEDataRetriever()
df = retriever.get_data(index_type, from_date, to_date)
```

- `index_type` (str): The specific NSE index you want to retrieve data for.
- `from_date` (str): Start date in `DD-MM-YYYY` format.
- `to_date` (str): End date in `DD-MM-YYYY` format.

### Available Indices

The library provides four categories of indices. You must choose the `index_type` from one of the following lists:

#### Broad Indices

- NIFTY 50
- NIFTY NEXT 50
- NIFTY MIDCAP 50
- NIFTY MIDCAP 100
- NIFTY MIDCAP 150
- NIFTY SMALLCAP 50
- NIFTY SMALLCAP 100
- NIFTY SMALLCAP 250
- NIFTY MIDSMALLCAP 400
- NIFTY 100
- NIFTY 200
- NIFTY500 MULTICAP 50:25:25
- NIFTY LARGEMIDCAP 250
- NIFTY MIDCAP SELECT
- NIFTY TOTAL MARKET
- NIFTY MICROCAP 250
- NIFTY 500
- NIFTY500 LARGEMIDSMALL EQUAL-CAP WEIGHTED

#### Sectoral Indices

- NIFTY AUTO
- NIFTY BANK
- NIFTY ENERGY
- NIFTY FINANCIAL SERVICES
- NIFTY FINANCIAL SERVICES 25/50
- NIFTY FMCG
- NIFTY IT
- NIFTY MEDIA
- NIFTY METAL
- NIFTY PHARMA
- NIFTY PSU BANK
- NIFTY REALTY
- NIFTY PRIVATE BANK
- NIFTY HEALTHCARE INDEX
- NIFTY CONSUMER DURABLES
- NIFTY OIL & GAS
- NIFTY MIDSMALL HEALTHCARE
- NIFTY FINANCIAL SERVICES EX-BANK
- NIFTY MIDSMALL FINANCIAL SERVICES
- NIFTY MIDSMALL IT & TELECOM

#### Thematic Indices

- NIFTY COMMODITIES
- NIFTY INDIA CONSUMPTION
- NIFTY CPSE
- NIFTY INFRASTRUCTURE
- NIFTY MNC
- NIFTY GROWTH SECTORS 15
- NIFTY PSE
- NIFTY SERVICES SECTOR
- NIFTY100 LIQUID 15
- NIFTY MIDCAP LIQUID 15
- NIFTY INDIA DIGITAL
- NIFTY100 ESG
- NIFTY INDIA MANUFACTURING
- NIFTY INDIA CORPORATE GROUP INDEX - TATA GROUP 25% CAP
- NIFTY500 MULTICAP INDIA MANUFACTURING 50:30:20
- NIFTY500 MULTICAP INFRASTRUCTURE 50:30:20
- NIFTY INDIA DEFENCE
- NIFTY INDIA TOURISM
- NIFTY CAPITAL MARKETS
- NIFTY EV & NEW AGE AUTOMOTIVE
- NIFTY INDIA NEW AGE CONSUMPTION
- NIFTY INDIA SELECT 5 CORPORATE GROUPS (MAATR)
- NIFTY MOBILITY
- NIFTY100 ENHANCED ESG
- NIFTY CORE HOUSING
- NIFTY HOUSING
- NIFTY IPO
- NIFTY MIDSMALL INDIA CONSUMPTION
- NIFTY NON-CYCLICAL CONSUMER
- NIFTY RURAL
- NIFTY SHARIAH 25
- NIFTY TRANSPORTATION & LOGISTICS
- NIFTY50 SHARIAH
- NIFTY500 SHARIAH

#### Strategic Indices

- NIFTY DIVIDEND OPPORTUNITIES 50
- NIFTY50 VALUE 20
- NIFTY100 QUALITY 30
- NIFTY50 EQUAL WEIGHT
- NIFTY100 EQUAL WEIGHT
- NIFTY100 LOW VOLATILITY 30
- NIFTY ALPHA 50
- NIFTY200 QUALITY 30
- NIFTY ALPHA LOW-VOLATILITY 30
- NIFTY200 MOMENTUM 30
- NIFTY MIDCAP150 QUALITY 50
- NIFTY200 ALPHA 30
- NIFTY MIDCAP150 MOMENTUM 50
- NIFTY500 MOMENTUM 50
- NIFTY MIDSMALLCAP400 MOMENTUM QUALITY 100
- NIFTY SMALLCAP250 MOMENTUM QUALITY 100
- NIFTY TOP 10 EQUAL WEIGHT
- NIFTY ALPHA QUALITY LOW-VOLATILITY 30
- NIFTY ALPHA QUALITY VALUE LOW-VOLATILITY 30
- NIFTY HIGH BETA 50
- NIFTY LOW VOLATILITY 50
- NIFTY QUALITY LOW-VOLATILITY 30
- NIFTY SMALLCAP250 QUALITY 50
- NIFTY TOP 15 EQUAL WEIGHT
- NIFTY100 ALPHA 30
- NIFTY200 VALUE 30
- NIFTY500 EQUAL WEIGHT
- NIFTY500 MULTICAP MOMENTUM QUALITY 50
- NIFTY500 VALUE 50
- NIFTY TOP 20 EQUAL WEIGHT

## Examples

### Basic Example

```python
from nse_data_retriever import NSEDataRetriever

# Initialize the retriever
retriever = NSEDataRetriever()

# Define parameters
index_type = "NIFTY 50"
from_date = "01-01-2023"
to_date = "31-01-2023"

# Retrieve data
try:
    data = retriever.get_data(index_type, from_date, to_date)
    print(data.head())
except Exception as e:
    print(f"An error occurred: {e}")
```

### Listing Available Indices

```python
from nse_data_retriever import Broad_Indices, Sectoral_Indices, Thematic_Indices, Strategic_Indices

print("Broad Indices:")
for index in Broad_Indices:
    print(f"- {index}")

print("\nSectoral Indices:")
for index in Sectoral_Indices:
    print(f"- {index}")

print("\nThematic Indices:")
for index in Thematic_Indices:
    print(f"- {index}")

print("\nStrategic Indices:")
for index in Strategic_Indices:
    print(f"- {index}")
```

### Handling Invalid Index Type

```python
from nse_data_retriever import NSEDataRetriever

retriever = NSEDataRetriever()

# Invalid index type
index_type = "INVALID INDEX"
from_date = "01-01-2023"
to_date = "31-01-2023"

try:
    data = retriever.get_data(index_type, from_date, to_date)
except ValueError as ve:
    print(ve)
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make Your Changes**

4. **Commit Your Changes**

   ```bash
   git commit -m "Add your message here"
   ```

5. **Push to the Branch**

   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Open a Pull Request**

Please ensure your code adheres to the existing style and includes appropriate tests.

## License

This project is licensed under the [MIT License](LICENSE).
---

*Happy Coding!*
