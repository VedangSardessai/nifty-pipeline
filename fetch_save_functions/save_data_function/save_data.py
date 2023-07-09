from datetime import datetime
from data_cleaning_function.cleanCSV import clean_transform_data


def save_data_to_csv(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"historicalData/nifty_data_{timestamp}.csv"
    cleaned_output_file = f"cleanedHistoricalData/cleaned_nifty_data_{timestamp}.csv"

    data_reset_index = data.reset_index()
    data_reset_index['Date'] = data_reset_index['Date'].dt.strftime('%d-%m-%Y')
    data_reset_index.to_csv(output_file, index=False)

    data_reset_index.drop('Adj Close', axis=1, inplace=True)
    data_reset_index.to_csv(output_file, index=False)

    clean_transform_data(output_file, cleaned_output_file)
    print("Data saved to", output_file)

