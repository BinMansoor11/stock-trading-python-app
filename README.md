# 📈 Stock Trading Python App

This Python script fetches **all active stock tickers** from the [Polygon.io API](https://polygon.io/) and saves them to a CSV file for later use in trading strategies, analysis, or data pipelines.

---

## 🚀 Features

- Retrieves **all active stock tickers** from Polygon.io using the `/v3/reference/tickers` endpoint.
- Handles **pagination** via `next_url` until all tickers are collected.
- Saves ticker data to a CSV file (`tickers.csv`) with a fixed schema.
- Uses **dotenv** for secure API key management.

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/stock-trading-python-app.git
   cd stock-trading-python-app
   ```
