import pandas as pd
import subprocess
import os
import sys

# Function to remove columns with 10% or more missing values from a DataFrame
def remove_sparse_columns(df, threshold=0.1):
    threshold_count = len(df) * threshold
    return df.dropna(thresh=threshold_count, axis=1)

# Function to preprocess uploaded CSV files
def preprocess_uploaded_files(file_paths):
    data_frames = []

    for file_path in file_paths:
        df = pd.read_csv(file_path, low_memory=False)
        cleaned_df = remove_sparse_columns(df)
        data_frames.append(cleaned_df)

    # Merge the cleaned DataFrames
    merged_data = pd.concat(data_frames)

    # Save the merged data to a new CSV file
    merged_data.to_csv('merged_data.csv', index=False)

    # Execute the Classified.py script
    subprocess.run(["python3", os.path.join(script_directory, "Classified.py")])  # Change python3 to python if on Windows

if __name__ == '__main__':
    # Get file paths from command-line arguments
    file_paths = sys.argv[1:]

    # Specify the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    preprocess_uploaded_files(file_paths)
