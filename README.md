# Weather-App-API

Weather App API:
A simple desktop weather app using PyQt5 and OpenWeatherMap.

Features

	•	Enter any city name and click 'Get Weather'
	•	Displays current temperature, weather description, and icon
	•	Shows 5‑day forecast (daily average temperatures)

Requirements:

	•	Python 3.x
	•	PyQt5
	•	requests

Installation:

1.	Clone the repo;

  		git clone https://github.com/yourusername/weather-app-api.git
  		cd weather-app-api


2. Install the requried Library;

  		pip install PyQt5 requests



Configuration:

	Open main.py and replace the api_key value with your OpenWeatherMap API key;
  
  	api_key = "your_api_key_here"

-----

Running the App

From the project directory, Run:

python main.py

	•	A window will open.
	•	Type a city name into the text box.
	•	Click Get Weather to load current weather and forecast.
