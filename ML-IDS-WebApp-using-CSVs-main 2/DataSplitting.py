import pandas as pd
from sklearn.model_selection import train_test_split
import subprocess
import os

# Read your dataset
data = pd.read_csv('classified_data_with_anomaly.csv')  # Replace with your actual file path

# Separate anomalies and non-anomalies
anomalies = data[data['Anomalous'] == True]  # Assuming 'True' indicates anomalies
non_anomalies = data[data['Anomalous'] == False]

# Split anomalies and non-anomalies into training and testing sets
anomalies_train, anomalies_test = train_test_split(anomalies, test_size=0.2, random_state=42)
non_anomalies_train, non_anomalies_test = train_test_split(non_anomalies, test_size=0.2, random_state=42)

# Concatenate anomalies and non-anomalies for training and testing sets
train_data = pd.concat([anomalies_train, non_anomalies_train], ignore_index=True)
test_data = pd.concat([anomalies_test, non_anomalies_test], ignore_index=True)

script_directory = os.path.dirname(os.path.abspath(__file__))
# Save the split datasets to CSV files
train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)
subprocess.run(["python3", os.path.join(script_directory, "more_logisticreg.py")]) #Change python3 to python for Windows