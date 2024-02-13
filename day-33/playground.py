import requests

MY_LAT = 51.507351
MY_LNG = 0.127758

# //------------------------ Get to know how API works ------------------------//
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# data = response.json()["iss_position"]
#
# longitude = data["longitude"]
# latitude = data["latitude"]
#
# iss_positions = (latitude, longitude)
# print(iss_positions)
#
# iss_positions = ()
# print(iss_positions)

# //------------------------ How to work with the sunset ------------------------//
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()