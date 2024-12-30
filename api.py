import requests
import pandas as pd
from google.cloud import bigquery
import os
# Make a GET request to the API
response = requests.get("https://randomuser.me/api")
data = response.json()

# Extract the 'results' key
results_data = data['results']

# Normalize the JSON data
df = pd.json_normalize(results_data)

# Extract the first and last names
df['Full Name'] = df['name.title'] + ' ' + df['name.first'] + ' ' + df['name.last']

names_df = df[['Full Name']]
# Select only the relevant column

credentials_path = r"C:\Users\block360_\Desktop\Zeeshan Data\Project"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()

table_id = "bubbly-enigma-444309-h2.Shops.name"

job = client.load_table_from_dataframe(names_df, table_id)

job.result()

print(f"Data successfully loaded into BigQuery table {table_id}")
