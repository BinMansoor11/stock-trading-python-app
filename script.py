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
tickers = []

def safe_request(url, retries=5, backoff=2):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error: {e}, retrying in {backoff} seconds...")
            time.sleep(backoff)
            backoff *= 2
    raise Exception(f"Failed after {retries} retries")

response = safe_request(url)
for ticker in response['results']:
    tickers.append(ticker)

while 'next_url' in response:
    time.sleep(10)
    response = safe_request(response['next_url'] + f'&apiKey={POLYGON_API_KEY}')
    for ticker in response['results']:
        tickers.append(ticker)

csv_columns = [
	'ticker', 'name', 'market', 'locale', 'primary_exchange', 'type', 'active',
	'currency_name', 'cik', 'composite_figi', 'share_class_figi', 'last_updated_utc'
]

with open('tickers.csv', 'w', newline='', encoding='utf-8') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
	writer.writeheader()
	for ticker in tickers:
		row = {col: ticker.get(col, '') for col in csv_columns}
		writer.writerow(row)