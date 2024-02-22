import requests
from datetime import datetime
import smtplib
import sched, time

MY_LAT = 51.924419  # Your latitude
MY_LONG = -4.477733  # Your longitude
MY_EMAIL = "toadenstartoad@gmail.com"
MY_PASSWORD = "enjnpdavufscuhwc"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# -------------------- run every 60 seconds -------------------------------------
def is_night():
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
    hour_now = time_now.hour

    print(sunrise)
    print(sunset)
    if hour_now >= sunrise or hour_now <= sunset:
        return True


# If the ISS is close to my current position
if is_iss_overhead() and is_night():
    def do_something(scheduler):
        scheduler.enter(60, 1, do_something, (scheduler,))
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="dannyduyanhnguyen@outlook.com",
                msg=f"Subject:The sun is setting!\n\nLook up right now! The sun is setting! Danny Nguyen"
            )
            print("Passed, Look up!!")


    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(1, 1, do_something, (my_scheduler,))
    my_scheduler.run()
else:
    print("Failed")


# and it is currently dark
# Then send me an email to tell me to look up.


# BONUS: run the code every 60 seconds.
