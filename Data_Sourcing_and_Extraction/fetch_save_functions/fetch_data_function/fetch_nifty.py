from datetime import datetime, timedelta
import yfinance as yf


def fetch_nifty_data():
    ticker = "^NSEI"  # Ticker symbol for NIFTY index
    start_date = '2007-09-17'
    end_date = (timedelta(days=1) + datetime.now()).strftime("%Y-%m-%d")
    data = yf.download(ticker, start=start_date, end=end_date)
    return data
