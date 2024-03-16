# BiciMad ML Improvement Project 🚵

✅Description
This project is a Flask-based web application designed to interact with the BiciMAD API, Madrid's public bicycle sharing system. It provides users with the ability to retrieve information about BiciMAD stations, test API connections, and access the BiciMAD Go zones.

✅Features
User authentication to access the BiciMAD API.
Fetching the list of BiciMAD stations and displaying them as JSON.
Testing the connection to the BiciMAD API and verifying token receipt.
Retrieving and displaying BiciMAD Go zones as JSON.
Rendered pages for various application states including the homepage, EDA (Exploratory Data Analysis), ML project information, and user application interface.

✅Installation

Clone this repository.

Create a virtual environment:
python -m venv venv

Activate the virtual environment:

On Windows:
venv\Scripts\activate

On Unix or MacOS:
source venv/bin/activate
Install the required packages:
pip install -r requirements.txt

✅Run the application:

python app.py
Usage
After starting the application, navigate to http://127.0.0.1:5000/ to view the homepage.

/: The root directory serves the homepage.
/estaciones: Returns a JSON list of BiciMAD stations.
/test_conexion: Tests the API connection and returns the access token upon success.
/bicimadgo: Fetches and displays the available BiciMAD Go zones in JSON format.
Additional routes for /eda, /proyectoml, and /appuser render their respective templates.
Configuration
You must supply your BiciMAD API credentials to use this application. Replace the placeholder email and password in the iniciar_sesion function with your actual BiciMAD API credentials.

✅Disclaimer
This project is intended for educational purposes. Do not use real credentials or API tokens within the source code when sharing publicly.

✅Contribution
Contributions are welcome. Please fork the repository and submit a pull request for review.
