import pandas as pd
import numpy as np
import subprocess
import os

def classify_anomalies(input_file_path, output_file_path):
    # Read the dataset
    data = pd.read_csv(input_file_path)

    # Define columns related to potential attacks
    attack_columns = ['orig_bytes', 'resp_bytes', 'conn_state', 'history', 'missed_bytes']

    def detect_anomalies(row):
        if row['orig_bytes'] > 100 or row['resp_bytes'] > 100:
            return True, 'Possible DDoS attack - Unusually high bytes sent or received'
        elif row['conn_state'] == 'REJ' and (row['orig_pkts'] > 10 or row['resp_pkts'] > 10):
            return True, 'Possible Port Scan - High packets exchanged with REJ connection state'
        elif isinstance(row['history'], str) and 'R' in row['history']:
            return True, 'Possible Reconnaissance - Anomalous history with "R"'
        elif isinstance(row['history'], float) and np.isnan(row['history']):
            return False, 'No issues till now'
        elif row['missed_bytes'] > 0:
            return True, 'Possible Intrusion - Missed bytes detected'
        elif row['orig_ip_bytes'] > 100 or row['resp_ip_bytes'] > 100:
            return True, 'Possible Data Exfiltration - Unusually high IP bytes sent or received'
        else:
            return False, 'No issues till now'

    # Apply the function to each row to classify the data
    data['Anomalous'], data['Anomaly_Description'] = zip(*data.apply(detect_anomalies, axis=1))

    # Assuming 'ts' column contains timestamps, converting it to datetime format
    data['ts'] = pd.to_datetime(data['ts'])

    # Define a time interval for grouping in minutes (e.g., per 5 minutes)
    time_interval = '5T'  # Change this to suit your analysis (e.g., '5T' for 5-minute intervals)

    # Group data by time intervals and count rejection instances per interval
    rejection_count = data[data['conn_state'] == 'REJ'].groupby(pd.Grouper(key='ts', freq=time_interval)).size()

    # Calculate rejection rate per time interval
    total_events = data.groupby(pd.Grouper(key='ts', freq=time_interval)).size()
    rejection_rate = rejection_count / total_events

    # Define a threshold for identifying anomalous rejection rates
    threshold = 0.1  # Adjust this threshold based on your dataset and requirements

    # Identify anomalies based on rejection rates exceeding the threshold
    anomalous_intervals = rejection_rate[rejection_rate > threshold]

    # Save the updated dataset with the anomaly classification
    data.to_csv(output_file_path, index=False)

    # Print or analyze anomalous intervals
    print(anomalous_intervals)
script_directory = os.path.dirname(os.path.abspath(__file__))
# Example usage
input_file_path = 'merged_data.csv'
output_file_path = 'classified_data_with_anomaly.csv'
classify_anomalies(input_file_path, output_file_path)
subprocess.run(["python3", os.path.join(script_directory, "DataSplitting.py")]) # Change python3 to python for Windows