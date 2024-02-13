import requests

MY_LAT = 51.507351
MY_LNG = 0.127758

# //------------------------ Get to know how API works ------------------------//
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

# //------------------------ How to work with the sunset ------------------------//
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)