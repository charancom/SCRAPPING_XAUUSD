import requests
import pandas as pd

# Tiingo API Tokenb91e3189ab58b44b012171425bb8c35c683e8d39
api_token = "b91e3189ab58b44b012171425bb8c35c683e8d39"

# Base API URL for Forex
base_url = "https://api.tiingo.com/tiingo/fx"

# Function to get top-of-book data for XAUUSD
def get_top_of_book(ticker="XAUUSD"):
    url = f"{base_url}/{ticker}/top"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {api_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching top-of-book data: {response.status_code} - {response.text}")
        return None

# Function to get historical intraday prices for XAUUSD
def get_historical_prices(ticker="XAUUSD", start_date="2024-10-01", resample_freq="15min"):
    url = f"{base_url}/{ticker}/prices"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {api_token}"
    }
    params = {
        "startDate": start_date,
        "resampleFreq": resample_freq
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching historical prices: {response.status_code} - {response.text}")
        return None

# Save data to DataFrame and CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Example Usage
if __name__ == "__main__":
    # Get real-time top-of-book data
    top_of_book_data = get_top_of_book()
    if top_of_book_data:
        print("Top-of-Book Data:")
        print(top_of_book_data)
        save_to_csv([top_of_book_data], "Data_Scraped/top_of_book_15_Min.csv")  # Save as CSV

    # Get historical intraday prices
    historical_prices_data = get_historical_prices()
    if historical_prices_data:
        print("Historical Prices Data:")
        save_to_csv(historical_prices_data, "Data_Scraped/historical_prices_15_Min.csv")  # Save as CSV
