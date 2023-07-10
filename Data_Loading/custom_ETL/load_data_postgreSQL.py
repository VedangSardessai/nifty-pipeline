import csv
from db.db_init import conn

def load_csv_to_postgres(csv_file_path):
    table_name = "nifty_data"
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        date DATE,
        open DECIMAL,
        high DECIMAL,
        low DECIMAL,
        close DECIMAL,
        volume INT
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Open the CSV file and load its contents into the PostgreSQL table
    with open(csv_file_path, 'r') as file:
        # Skip the header row if it exists
        next(file)

        # Create a CSV reader object
        csv_reader = csv.reader(file)

        # Prepare the INSERT query
        insert_query = f"""
        INSERT INTO {table_name} (date, open, high, low, close, volume)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        # Iterate over each row in the CSV file and insert the data into the table
        for row in csv_reader:
            date = row[0]
            open_price = row[1]
            high_price = row[2]
            low_price = row[3]
            close_price = row[4]
            volume = row[5]

            cursor.execute(insert_query, (date, open_price, high_price, low_price, close_price, volume))

        # Commit the changes to the database
        conn.commit()

    # Close the cursor and database connection
    cursor.close()


    print("Data loaded into the PostgreSQL table.")
