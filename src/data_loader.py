import yfinance as yf
import pandas as pd
def load_stock_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    data.to_csv(f"data/raw/{ticker}_raw.csv")
    return data

