from datetime import datetime
import yfinance as yf


def fetch_nifty_data():
    ticker = "RELIANCE.NS"  # Ticker symbol for NIFTY index
    start_date = '2007-09-17'
    end_date = datetime.now().strftime("%Y-%m-%d")
    data = yf.download(ticker, start=start_date, end=end_date)
    return data
