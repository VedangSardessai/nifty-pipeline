import pandas as pd


def clean_transform_data(input_file, output_file):
    # Read the raw data from the CSV file
    raw_data = pd.read_csv(input_file)

    # Drop any rows with missing values
    cleaned_data = raw_data.dropna()

    # Round the 'Open', 'High', 'Low', and 'Close' columns to integers (without decimal places)
    cleaned_data['Open'] = cleaned_data['Open'].round(decimals=0).astype(int)
    cleaned_data['High'] = cleaned_data['High'].round(decimals=0).astype(int)
    cleaned_data['Low'] = cleaned_data['Low'].round(decimals=0).astype(int)
    cleaned_data['Close'] = cleaned_data['Close'].round(decimals=0).astype(int)

    # Perform additional data transformations and cleaning operations as needed
    # Example: Convert data types, handle missing values, normalize data, perform currency conversion, etc.

    # Save the cleaned and transformed data to a new CSV file
    cleaned_data.to_csv(output_file, index=False)
    print("Cleaned and transformed data saved to", output_file)
