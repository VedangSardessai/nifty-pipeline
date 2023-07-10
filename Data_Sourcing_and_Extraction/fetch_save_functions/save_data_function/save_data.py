from datetime import datetime
from Data_Transformation.data_cleaning_function.cleanCSV import clean_transform_data
from Data_Loading.custom_ETL.load_data_postgreSQL import load_csv_to_postgres


def save_data_to_csv(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"Nifty_data_CSV/fetched_data_csv/nifty_data_{timestamp}.csv"
    cleaned_output_file = f"Nifty_data_CSV/transformed_data_csv/cleaned_nifty_data_{timestamp}.csv"

    data_reset_index = data.reset_index()
    data_reset_index['Date'] = data_reset_index['Date'].dt.strftime('%Y-%m-%d')
    data_reset_index.to_csv(output_file, index=False)

    data_reset_index.drop('Adj Close', axis=1, inplace=True)
    data_reset_index.to_csv(output_file, index=False)

    clean_transform_data(output_file, cleaned_output_file)
    print("Data saved to", cleaned_output_file)

    # Print the data profile

    load_csv_to_postgres(cleaned_output_file)

