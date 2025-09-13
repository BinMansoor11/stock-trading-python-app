import requests
import openai
import os
import time
import csv
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY= os.getenv("POLYGON_API_KEY")

LIMIT= 1000

url=f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'

response= requests.get(url)
tickers = []

data = response.json()
for ticker in data['results']:
    tickers.append(ticker)

while 'next_url' in data:
    time.sleep(10)
    response = requests.get(data['next_url'] + f'&apiKey={POLYGON_API_KEY}')
    data = response.json()
    for ticker in data['results']:
        tickers.append(ticker)


# Write tickers to CSV with the same schema as example_ticker
csv_columns = [
	'ticker', 'name', 'market', 'locale', 'primary_exchange', 'type', 'active',
	'currency_name', 'cik', 'composite_figi', 'share_class_figi', 'last_updated_utc'
]

with open('tickers.csv', 'w', newline='', encoding='utf-8') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
	writer.writeheader()
	for ticker in tickers:
		# Only write keys that match the schema, fill missing keys with empty string
		row = {col: ticker.get(col, '') for col in csv_columns}
		writer.writerow(row)