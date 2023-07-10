from dotenv import dotenv_values
import psycopg2
import csv

env_vars = dotenv_values('.env')
username = env_vars['USERNAME']
password = env_vars['PASSWORD']
database_name = env_vars['DBNAME']
port = env_vars['PORT']
table_name = "nifty_data"

# Database connection details
db_host = 'localhost'
db_port = port
db_name = database_name
db_user = username
db_password = password


def load_csv_to_postgres(csv_file_path):
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )

    # Create a cursor object to execute SQL queries
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
    conn.close()

    print("Data loaded into the PostgreSQL table.")
