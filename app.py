from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# OpenWeatherMap API key (replace with your API key)
API_KEY = 'f18acc43e2da39df93a8293f004bea83'

# Load the pre-trained SVM model
svm_model = joblib.load('flood_risk_svm_model.pkl')

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')

    # Fetch weather data from OpenWeatherMap API
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
    response = requests.get(weather_url)
    data = response.json()

    if response.status_code == 200:
        # Extract weather features from the API response
        rainfall = data.get('rain', {}).get('1h', 0)  # Rainfall in mm in the last hour
        temperature = data['main']['temp']            # Temperature in °C
        humidity = data['main']['humidity']           # Humidity percentage
        wind_speed = data['wind']['speed']            # Wind speed in m/s

        # Prepare the features for the model
        features = np.array([[temperature, wind_speed, humidity]])

        # Use the SVM model to predict flood risk (0 or 1)
        flood_risk_prediction = svm_model.predict(features)[0]

        flood_risk = "High Risk of Flood" if flood_risk_prediction == 1 else "Low Risk of Flood"

        # Prepare the response data
        weather_info = {
            'location': data['name'],
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'flood_risk': flood_risk
        }

        return jsonify(weather_info), 200
    else:
        return jsonify({'error': 'Location not found or API request failed'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
