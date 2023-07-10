from datetime import datetime
from Data_Transformation.data_cleaning_function.cleanCSV import clean_transform_data
from Data_Loading.custom_ETL.load_data_postgreSQL import load_csv_to_postgres
from Data_Analytics.TIme_Series_Analysis.moving_averages import load_moving_average
from Data_Analytics.TIme_Series_Analysis.exponential_smoothing import calculate_exponential_smoothing
from Data_Analytics.TIme_Series_Analysis.autocorrelation import calculate_autocorrelation
from Data_Analytics.TIme_Series_Analysis.decomposition import perform_decomposition



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
    load_moving_average(cleaned_output_file, window=10)
    calculate_exponential_smoothing(cleaned_output_file, 0.25)
    # perform_decomposition(cleaned_output_file)
    calculate_autocorrelation(cleaned_output_file, 25)
