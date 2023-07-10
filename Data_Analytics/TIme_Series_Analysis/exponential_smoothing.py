import pandas as pd
import psycopg2
from db.db_init import conn

def calculate_exponential_smoothing(csv_file, alpha):
    """
    Calculate the exponential smoothing of a time series data and store it in a PostgreSQL table.
    :param csv_file: Path to the CSV file containing the NIFTY historical data.
    :param alpha: Smoothing factor (0 < alpha < 1).
    :return: None
    """
    # Read data from CSV file
    data = pd.read_csv(csv_file)
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

    # Calculate exponential smoothing
    exponential_smoothing = data['Close'].ewm(alpha=alpha, adjust=False).mean()

    # Connect to PostgreSQL database


    # Create table in PostgreSQL
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exponential_smoothing_of_nifty (
            date DATE,
            exponential_smoothing NUMERIC
        )
    """)
    conn.commit()

    # Insert data into PostgreSQL table
    for date, es in zip(data['Date'], exponential_smoothing):
        cursor.execute("""
            INSERT INTO exponential_smoothing_of_nifty (date, exponential_smoothing)
            VALUES (%s, %s)
        """, (date.date(), es))
    conn.commit()

    # Close the database connection
    cursor.close()
