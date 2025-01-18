import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import json

# Load your data
data = pd.read_csv('classified_data_with_anomaly.csv')

# Convert 'ts' column to datetime
data['ts'] = pd.to_datetime(data['ts'])

# Filter only anomalous data
anomalous = data[data['Anomalous']]

# Plot histogram for anomalous data
plt.figure(figsize=(12, 6))
plt.hist(anomalous['ts'], bins=50, alpha=0.7, color='red')
plt.xlabel('Timestamp (ts)')
plt.ylabel('Count')
plt.title('Anomalous Data Distribution based on Timestamp')
plt.savefig('anomalous_distribution_plot.png')  # Save the plot as an image
plt.close()  # Close the plot to prevent it from being displayed

# Load the training and testing datasets
train_data = pd.read_csv('train_data.csv')
test_data = pd.read_csv('test_data.csv')

# Separate features and target variable
X_train = train_data.drop('Anomalous', axis=1)
y_train = train_data['Anomalous']

X_test = test_data.drop('Anomalous', axis=1)
y_test = test_data['Anomalous']

# Encode categorical columns using Label Encoder
label_encoder = LabelEncoder()

for column in X_train.columns:
    if X_train[column].dtype == 'object':
        X_train[column] = label_encoder.fit_transform(X_train[column])

for column in X_test.columns:
    if X_test[column].dtype == 'object':
        X_test[column] = label_encoder.fit_transform(X_test[column])

# Impute missing values
imputer = SimpleImputer(strategy='mean')  # You can choose other strategies like 'median', 'most_frequent', etc.
X_train_imputed = pd.DataFrame(imputer.fit_transform(X_train), columns=X_train.columns)
X_test_imputed = pd.DataFrame(imputer.transform(X_test), columns=X_test.columns)

# Train a Logistic Regression model with increased max_iter
model = LogisticRegression(max_iter=5000)  # You can adjust the value based on your needs
model.fit(X_train_imputed, y_train)

# Make predictions on the test set
predictions = model.predict(X_test_imputed)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

# Confusion Matrix
cm = confusion_matrix(y_test, predictions)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['Normal', 'Anomalous'], yticklabels=['Normal', 'Anomalous'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.savefig('confusion_matrix_plot.png')  # Save the plot as an image
plt.close()  # Close the plot to prevent it from being displayed

# Classification Report
report = classification_report(y_test, predictions)
with open('classification_report.txt', 'w') as report_file:
    report_file.write(report)

# Prepare results as a dictionary
results = {
    'accuracy': accuracy,
    'confusion_matrix': cm.tolist(),
    'classification_report': report
}

# Save the results as a JSON file
with open('results.json', 'w') as json_file:
    json.dump(results, json_file)
