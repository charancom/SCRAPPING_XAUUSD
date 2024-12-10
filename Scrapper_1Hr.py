import requests
import pandas as pd

# Tiingo API Token
api_token = "b91e3189ab58b44b012171425bb8c35c683e8d39"

# Base API URL for Forex
base_url = "https://api.tiingo.com/tiingo/fx"

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

def get_historical_prices(ticker="XAUUSD", start_date="2024-10-01", resample_freq="1Hour"):
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

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    top_of_book_data = get_top_of_book()
    if top_of_book_data:
        print("Top-of-Book Data:")
        print(top_of_book_data)
        save_to_csv([top_of_book_data], "Data_Scraped/top_of_book_1_Hour.csv")  # Save as CSV

    historical_prices_data = get_historical_prices()
    if historical_prices_data:
        print("Historical Prices Data:")
        save_to_csv(historical_prices_data, "Data_Scraped/historical_prices_1_Hour.csv")  # Save as CSV
