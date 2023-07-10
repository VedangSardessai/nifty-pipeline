import pandas as pd
import psycopg2
from db.db_init import conn


def load_moving_average(csv_file, window):
    """
    Calculate the moving average of a time series data and store it in a PostgreSQL table.
    :param csv_file: Path to the CSV file containing the NIFTY historical data.
    :param window: Number of periods to consider for the moving average.
    :return: None
    """
    # Read data from CSV file
    data = pd.read_csv(csv_file)
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')
    moving_average = data['Close'].rolling(window=window).mean()


    # Create table in PostgreSQL
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS moving_average_of_nifty (
            date DATE,
            moving_average NUMERIC
        )
    """)
    conn.commit()

    # Insert data into PostgreSQL table
    for date, ma in zip(data['Date'], moving_average):
        cursor.execute("""
            INSERT INTO moving_average_of_nifty (date, moving_average)
            VALUES (%s, %s)
        """, (date.date(), ma))
    conn.commit()

    # Close the database connection
    cursor.close()

