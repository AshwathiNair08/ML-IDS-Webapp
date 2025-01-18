from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import subprocess
import os
import json

app = Flask(__name__)
CORS(app)
script_directory = os.path.dirname(os.path.abspath(__file__))

def remove_sparse_columns(df, threshold=0.9):
    threshold_count = len(df) * threshold
    return df.dropna(thresh=threshold_count, axis=1)

# Function to process and clean CSV files
def process_csv_files(file_list):
    data_frames = []
    for file_name in file_list:
        df = pd.read_csv(file_name, low_memory=False)
        cleaned_df = remove_sparse_columns(df)
        data_frames.append(cleaned_df)
    merged_data = pd.concat(data_frames)
    return merged_data

# Store the results and plot paths in global variables
global_results = None
global_plot_paths = {}

@app.route('/analyze', methods=['POST'])
def analyze_csv():
    try:
        uploaded_file = request.files['file']
        file_path = 'temp.csv'
        uploaded_file.save(file_path)

        # Ask the user if they want to proceed with preprocessing
        subprocess.run(["python3", os.path.join(script_directory, "Preprocessing.py"), file_path])

        return jsonify({'status': 'file_received', 'file_path': file_path})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/execute_preprocessing', methods=['POST'])
def execute_preprocessing():
    try:
        file_path = request.json.get('file_path')

        # Ask the user if they want to proceed with analysis
        subprocess.run(["python3", os.path.join(script_directory, "Classified.py"), file_path])

        # Read the results from the JSON file
        global global_results
        with open('results.json', 'r') as json_file:
            global_results = json.load(json_file)

        # Store the paths for the plots
        global global_plot_paths
        global_plot_paths['histogram'] = 'histogram_plot.png'
        global_plot_paths['confusion_matrix'] = 'confusion_matrix_plot.png'

        return jsonify({'status': 'preprocessing_completed'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_results', methods=['GET'])
def get_results():
    global global_results
    return jsonify(global_results)

@app.route('/get_plot/<plot_type>', methods=['GET'])
def get_plot(plot_type):
    try:
        # Check if the plot type is valid
        if plot_type in global_plot_paths:
            # Define the path for the plot
            plot_path = global_plot_paths[plot_type]
            
            # Check if the file exists
            if os.path.exists(plot_path):
                # Send the plot file to the client
                return send_file(plot_path, mimetype='image/png', as_attachment=True)
            else:
                return jsonify({'error': 'Plot not found'}), 404
        else:
            return jsonify({'error': 'Invalid plot type'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
