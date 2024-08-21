from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# Load feature names
with open('features.txt') as f:
    feature_columns = f.read().splitlines()

@app.route('/')
def home():
    return "Welcome to the DDoS Detection AI Model"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Convert data to DataFrame
        input_data = pd.DataFrame([data])

        # Ensure the columns are in the same order as the training data
        input_data = input_data[feature_columns]

        # Scale the data
        input_data_scaled = scaler.transform(input_data)

        # Make predictions
        predictions = model.predict(input_data_scaled)
        probabilities = model.predict_proba(input_data_scaled)[0][1]
        
        # Return the predictions as JSON
        return jsonify({
            'prediction': predictions.tolist(),
            'probability': probabilities.tolist(),
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
