import time
from fetch_save_functions.fetch_data_function.fetch_nifty import fetch_nifty_data
from fetch_save_functions.save_data_function.save_data import save_data_to_csv


while True:
    try:
        nifty_data = fetch_nifty_data()
        save_data_to_csv(nifty_data)

        time.sleep(86500)  # Fetch data every 60 seconds
    except Exception as e:
        print("An error occurred:", str(e))
        time.sleep(60)  # Wait for 60 seconds before retrying
