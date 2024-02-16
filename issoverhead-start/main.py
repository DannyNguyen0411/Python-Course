import requests
from datetime import datetime
import smtplib

MY_LAT = 51.924419 # Your latitude
MY_LONG = -4.477733 # Your longitude
MY_EMAIL = "toadenstartoad@gmail.com"
MY_PASSWORD = "enjnpdavufscuhwc"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude)
print(iss_latitude)

#Your position is within +5 or -5 degrees of the ISS position.
# Use if else statement check of it returns true or false as always.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(data)
print(sunrise)
print(sunset)

#If the ISS is close to my current position
if iss_longitude > sunrise and iss_longitude < sunset and iss_latitude > sunrise and iss_latitude < sunset:
    print("Passed")
else:
    print("Failed")

# and it is currently dark
# Then send me an email to tell me to look up.
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs="dannyduyanhnguyen@outlook.com",
#         msg=f"Subject:Gotta Go Fast\n\nI would like to test of this mail will work. Danny Nguyen"
#     )


# BONUS: run the code every 60 seconds.



