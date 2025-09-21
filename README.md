# 🌦️ Weather Alert System with Twilio
This project uses the OpenWeatherMap API to fetch weather forecasts and sends an SMS alert via Twilio if rain is expected. It’s a simple automation script that helps you stay prepared for rainy days.

🚀 Features

Fetches weather forecast data from OpenWeatherMap.

Checks weather condition codes to detect rain.

Sends an SMS notification using Twilio if rain is predicted.

Customizable for any location using latitude/longitude.

🛠️ Requirements

Python 3.8+

requests library

twilio library

OpenWeatherMap API key

Twilio account (with active number)

📦 Installation

Clone the repository:

git clone https://github.com/yourusername/weather-alert.git
cd weather-alert


Install dependencies:

pip install requests twilio


Set up your API keys:

Get an API key from OpenWeatherMap
.

Get account_sid and auth_token from Twilio
.

⚙️ Configuration

In weather.py, replace placeholders with your credentials:

api_key = "INSERT_OPENWEATHER_API_KEY"
account_sid = "INSERT_TWILIO_SID"
auth_token = "INSERT_TWILIO_AUTH_TOKEN"


Also update:

lat & lon → your location coordinates

from_ → your Twilio phone number

to → your phone number

▶️ Usage

Run the script:

python weather.py


If rain is forecast in the next few hours, you’ll receive an SMS:

Take your umbrella. It’s going to rain.

📌 Example Output
queued


The status queued means your SMS has been successfully scheduled by Twilio.
