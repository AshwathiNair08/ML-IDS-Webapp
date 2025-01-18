// script.js

function handleFile() {
    const fileInput = document.getElementById('fileInput');
    const fileInputLabel = document.querySelector('.fileInputLabel');
    const clearFilesText = document.getElementById('clearFiles');

    // Update the label text with the selected file names
    if (fileInput.files.length > 0) {
        const fileNames = Array.from(fileInput.files).map(file => file.name).join(', ');
        fileInputLabel.innerText = `Selected files: ${fileNames}`;
        clearFilesText.style.display = 'inline'; // Show the clear files text
    } else {
        fileInputLabel.innerText = 'Select CSV files';
        clearFilesText.style.display = 'none'; // Hide the clear files text
    }
}

// Function to display a confirmation alert
function displayConfirmationAlert(alertType, alertMessage, callback) {
    // Use window.confirm to show a built-in confirmation dialog
    const userResponse = window.confirm(`${alertType} Alert: ${alertMessage}\nDo you want to proceed?`);
    
    // Check if a callback function is provided and if userResponse is true
    if (callback && typeof callback === 'function' && userResponse) {
        callback();
    }
}

// Function to handle preprocessing step
function handlePreprocessing(file_path) {
    // Request user confirmation for preprocessing
    displayConfirmationAlert('Preprocessing', 'Do you want to proceed with preprocessing?', userResponse => {
        if (userResponse) {
            // Proceed with preprocessing
            initiatePreprocessing(file_path);
        } else {
            // Display cancellation message
            console.log('Preprocessing cancelled by the user.');
        }
    });
}

// Function to handle analysis step
function handleAnalysis() {
    const fileInput = document.getElementById('fileInput');

    if (fileInput.files.length === 0) {
        displayConfirmationAlert('Error', 'Please select a CSV file.');
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('http://localhost:5000/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'file_received') {
            // Display preprocessing alert
            displayConfirmationAlert('Success', 'File received. Initiating preprocessing...');
            initiatePreprocessing(data.file_path);
        } else {
            // Display error message
            displayConfirmationAlert('Error', `Error receiving file: ${data.error}`);
        }
    })
    .catch(error => {
        // Display error message
        displayConfirmationAlert('Error', `Error receiving file: ${error}`);
    });
}

function initiatePreprocessing(filePath) {
    // Trigger the execution of preprocessing scripts using the received file path
    fetch('http://localhost:5000/execute_preprocessing', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'file_path': filePath })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'preprocessing_completed') {
            // Display success message or update UI with preprocessing results
            displayConfirmationAlert('Success', 'Preprocessing completed.');
            // You can call another function to display preprocessing results here
            fetchResults(); // Fetch and display results
        } else {
            // Display error message
            displayConfirmationAlert('Error', `Error during preprocessing: ${data.error}`);
        }
    })
    .catch(error => {
        // Display error message
        displayConfirmationAlert('Error', `Error during preprocessing: ${error}`);
    });
}

// Function to display analysis results
function displayResults(results) {
    const resultContainer = document.getElementById('resultContainer');

    // Clear previous results
    resultContainer.innerHTML = '';

    // Assuming results is an object containing accuracy, confusion_matrix, and classification_report
    const accuracyElement = document.createElement('p');
    accuracyElement.innerText = `Accuracy: ${results.accuracy.toFixed(2)}`;
    resultContainer.appendChild(accuracyElement);

    // Display confusion matrix
    const confusionMatrixElement = document.createElement('div');
    confusionMatrixElement.innerHTML = '<h3>Confusion Matrix</h3>';
    const confusionMatrixTable = document.createElement('table');
    const cmData = results.confusion_matrix;
    for (let i = 0; i < cmData.length; i++) {
        const row = document.createElement('tr');
        for (let j = 0; j < cmData[i].length; j++) {
            const cell = document.createElement('td');
            cell.innerText = cmData[i][j];
            row.appendChild(cell);
        }
        confusionMatrixTable.appendChild(row);
    }
    confusionMatrixElement.appendChild(confusionMatrixTable);
    resultContainer.appendChild(confusionMatrixElement);

    // Display classification report
    const classificationReportElement = document.createElement('div');
    classificationReportElement.innerHTML = `<h3>Classification Report</h3><pre>${results.classification_report}</pre>`;
    resultContainer.appendChild(classificationReportElement);
}

function clearSelectedFiles() {
    const fileInput = document.getElementById('fileInput');
    const fileInputLabel = document.querySelector('.fileInputLabel');
    const clearFilesText = document.getElementById('clearFiles');

    // Clear the selected files and update the label text
    fileInput.value = null;
    fileInputLabel.innerText = 'Select CSV files';
    clearFilesText.style.display = 'none'; // Hide the clear files text
}

// Function to fetch and display results
function fetchResults() {
    fetch('http://localhost:5000/get_results')
    .then(response => response.json())
    .then(results => {
        displayResults(results);
    })
    .catch(error => {
        console.error('Error fetching results:', error);
    });
}