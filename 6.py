
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Initialize WebDriver (Replace 'chromedriver' with the path if necessary)
driver = webdriver.Chrome()
date = "oct6.2024"
# URL of the webpage
url = "https://www.forexfactory.com/calendar?day=" + date
driver.get(url)

data = []

from datetime import datetime

# Original date string
date_str = date

# Convert the date string to a datetime object
date_format = "%b%d.%Y"  # Format: abbreviated month, day, period, year
date_obj = datetime.strptime(date_str, date_format)
# If you need it in a specific format (e.g., "YYYY-MM-DD"), convert it back to a string
formatted_date = date_obj.strftime("%Y-%m-%d")

# Wait for the page to load (adjust time if needed)
driver.implicitly_wait(10)

def scrape_table():
    try:
        # Locate the table containing the data
        table = driver.find_element(By.CSS_SELECTOR, ".calendar__table")

        # Extract rows of the table
        rows = table.find_elements(By.CSS_SELECTOR, "tr")
        counter = 1
        last_valid_time = ""  # Variable to keep track of the last valid time

        # Loop through each row and extract the details
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) >= 7:
                if counter == 1:
                    time_value = columns[1].text.strip() if columns[0].text else ""
                    news = columns[5].text.strip() if columns[5].text else ""
                    impact_element = columns[4].find_element(By.TAG_NAME, "span")
                    impact = impact_element.get_attribute("title")  # Directly use the title attribute
                    counter = counter + 2
                else:
                    time_value = columns[0].text.strip() if columns[0].text else ""
                    news = columns[4].text.strip() if columns[4].text else ""
                    impact_element = columns[3].find_element(By.TAG_NAME, "span")
                    impact = impact_element.get_attribute("title")  # Directly use the title attribute

                # Handle null time values by propagating the last valid time
                if not time_value:  # If the current time is null
                    time_value = last_valid_time  # Take the last valid time
                else:
                    last_valid_time = time_value  # Update the last valid time

                # Append to the data list
                data.append({
                    "Date": formatted_date,
                    "Time": time_value,
                    "Impact": impact,
                    "news": news,
                })
            else:
                print("Skipped a row due to insufficient data.")
    except Exception as e:
        print(f"Error scraping table: Error")  # Handle the exception and print the error message

# Scrape the data for the single day
scrape_table()

# Save the data to a CSV file
df_1 = pd.DataFrame(data)
df_1.to_csv(formatted_date + ".csv")
