from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load the trained model
loaded_best_model = joblib.load('model.pkl')  # Replace with the path to your trained model file

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json  # Receive input data as JSON
        
        print(input_data)
        
        # Convert the input data into a DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Make predictions using the loaded model
        predictions = loaded_best_model.predict(input_df)

        predicted_value = int(predictions[0])
        
        # Return the predicted value as JSON
        response_data = {"prediction": predicted_value}
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)