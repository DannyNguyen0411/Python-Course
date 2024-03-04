import requests
from twilio.rest import Client


OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "4f4455732e97509fca04f6e8ca54215d"
account_sid = "AC448519ca4de763906272b7ec1576e221"
auth_token = "5ea47110085926aa742f127e9cd105fa"

weather_params = {
    "lat":  51.850460,
    "lon": 4.325670,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
the_list = response.json()["list"]
# weather_id = weather_data["list"][0]["weather"][0]["id"]
# if weather_id < 700:
#     print("Bring the Umbrella☂️")
# else:
#     print("No Umbrella😎")

# --------------This is how I solved it.💪---------------
weather_forecast = []
will_rain = False

for item in the_list:
    weather = item["weather"]
    for sub_item in weather:
        weather_id = sub_item["id"]
        weather_description = sub_item["description"]
        weather_info = [weather_id, weather_description]

        weather_forecast.append(weather_info)
        if weather_id < 700:
            will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+15162593956',
        to='+31610348622'
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Jij bent €500 verschuldigd! Klik nu op deze link om nu uw lasten te betalen: https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
        from_='+15162593956',
        to='+31610348622'
    )
    print(message.status)
    # body="Jij bent €500 verschuldigd! Klik nu op deze link om nu uw lasten te betalen: https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"

print(weather_forecast)

