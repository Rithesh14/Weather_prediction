import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "3bdead181017b5b3d20d0b955e857025"

account_sid = "ACba1a3f0a448ca6b935253284ec923e82"
auth_token = "fd0eec00832d539f1f4dbd6b17fc11e7"

weather_params = {
    "lat":19.012961,
    "lon":73.101221,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Take your umbrella. Its going to rain",
        from_='+17622206574',
        to='+919082270469'
    )
    print(message.status)