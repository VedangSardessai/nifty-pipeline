import pandas as pd
from db.db_init import conn

def calculate_autocorrelation(csv_file, lag):
    """
    Calculate the autocorrelation of a time series data and store it in a PostgreSQL table.
    :param csv_file: Path to the CSV file containing the NIFTY historical data.
    :param lag: Number of periods to consider for autocorrelation.
    :return: None
    """
    # Read data from CSV file
    data = pd.read_csv(csv_file)
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

    # Calculate autocorrelation
    autocorrelation = data['Close'].autocorr(lag=lag)

    # Connect to PostgreSQL database


    # Create table in PostgreSQL
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS autocorrelation_of_nifty (
            lag INT,
            autocorrelation NUMERIC
        )
    """)
    conn.commit()

    # Insert data into PostgreSQL table
    cursor.execute("""
        INSERT INTO autocorrelation_of_nifty (lag, autocorrelation)
        VALUES (%s, %s)
    """, (lag, autocorrelation))
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()
