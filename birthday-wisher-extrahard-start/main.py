##################### Extra Hard Starting Project ######################
import smtplib
import random
import datetime as dt
from pandas import pandas


MY_EMAIL = "toadenstartoad@gmail.com"
MY_PASSWORD = "uhijbidvecdjplgc"



now = dt.datetime.now()
print(now)

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv", index_col= False)
data_dict = data.to_dict()

year_dict = data_dict["year"]
print(data_dict["year"])
print(data_dict["month"])
print(data_dict["day"])

for item in year_dict:
    print(item)

for item in data_dict:
    print(item)
# birthday = f"{data["year"]}{data["month"]}{data["day"]}"
# print(birthday)


# 2. Check if today matches a birthday in the birthdays.csv
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs=f"{MY_EMAIL}",
#         msg=f"Subject:Happy Birthday!\n\nTest."
#     )
#     print("mail send")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




