import pandas as pd
import glob

# Path to your CSV files (adjust if the files are in a different folder)
csv_files = glob.glob("*.csv")  # This will get all CSV files in the current directory

# List to hold individual DataFrames
dfs = []

# Read each CSV file and append it to the list
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames vertically (row-wise)
merged_df = pd.concat(dfs, ignore_index=True)

# Remove the column 'Unnamed: 0' if it exists
if 'Unnamed: 0' in merged_df.columns:
    merged_df = merged_df.drop(columns=['Unnamed: 0'])

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("merged_output.csv", index=False)

print("CSV files merged successfully into 'merged_output.csv'.")
