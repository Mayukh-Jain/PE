Project Title: Flood Risk Prediction and Mitigation Using Random Forest ML Algorithm and Real-Time Weather Data

Objective: 
  The project aims to develop a flood risk prediction system using a Support Vector Machine (SVM) model, trained on key weather features such as rainfall, temperature, wind speed, and humidity. It integrates real-time weather data from the OpenWeatherMap API to assess flood risk for specific locations dynamically.

Overview:
  This project combines machine learning and real-time data processing to predict flood risks and provide actionable insights for flood mitigation. The SVM model is trained on historical weather data, mapping weather conditions to flood occurrences. A Flask-based backend processes API data and communicates the flood risk predictions to a user-friendly front-end web interface.

Key Features:
  Data Integration: Historical weather data and live data from APIs for accurate flood risk prediction.
  Machine Learning: SVM model trained to classify flood risk based on weather conditions.
  Real-Time Predictions: Uses live weather data to dynamically assess flood risks.
  Web Interface: A visually appealing and responsive front-end with video backgrounds and CSS styling.
  Mitigation Strategies: Includes detailed insights and strategies for flood prevention and response.
  
Potential Applications:
  Flood-prone areas for community safety and planning.
  Urban planning to identify and address vulnerable zones.
  Disaster management agencies for rapid response and preparedness.


Code Explaination:
1. Machine Learning Model Code
Objective:
This code trains a Support Vector Machine (SVM) model using features such as temperature, humidity, wind speed, and rainfall to predict whether flooding will occur.

Code Breakdown:

Data Loading and Preprocessing:

Reads the dataset (e.g., Bhubaneswar 2022.csv) containing historical weather data.
Handles missing values and normalizes the features to ensure proper scaling for the SVM algorithm.
Feature Selection:

Selects the relevant features (temperature, humidity, and wind speed) as inputs and flood occurrence (0 or 1) as the target.
Model Training:

Splits the data into training and testing sets.
Uses the SVC class from Scikit-learn to train the SVM model with a linear kernel for simplicity.
Evaluates the model using accuracy scores and classification reports.
Purpose:
This model forms the backbone of flood prediction by identifying patterns in historical data and predicting the likelihood of flooding under current weather conditions.

2. Flask Backend Code
Objective:
The Flask application serves as the backend, integrating the trained SVM model and real-time weather data fetched via the OpenWeatherMap API.

Code Breakdown:

Route for Weather Data:

/weather: Accepts a location parameter from the frontend.
Fetches real-time weather data (temperature, humidity, wind speed, and rainfall) using the OpenWeatherMap API.
Flood Risk Prediction:

Prepares the fetched weather data as inputs for the SVM model.
Passes the data through the trained SVM model to predict the flood risk (high risk or low risk).
API Integration:

Utilizes the OpenWeatherMap API for live weather data.
Parses the API response to extract key weather metrics.
Response to Frontend:

Returns the weather metrics and flood risk as a JSON object to be displayed on the web interface.
3. Frontend HTML & CSS Code
Objective:
The HTML and CSS files create a user-friendly interface for users to input a location and view flood risk predictions.

Code Breakdown:

HTML Structure:

Provides input fields for the location and a button to submit the query.
Displays real-time weather data (temperature, humidity, rainfall, wind speed) and flood risk.
CSS for Styling:

Implements a video background for aesthetics.
Styles the input fields, buttons, and output display for a clean and modern look.
JavaScript Integration:

Fetches data from the Flask backend using AJAX requests.
Dynamically updates the page with the weather data and flood risk prediction.
4. Final Integration
Process:

Start the Flask backend:

Run the Python script for the backend (app.py) to serve predictions via http://127.0.0.1:5000.
Open the HTML Frontend:

Load the HTML file in a browser (e.g., http://127.0.0.1:3000) using a local server.
Interact with the System:

Enter a location in the input field and submit.
The backend fetches live weather data, predicts the flood risk, and returns the result to be displayed on the web page.   
