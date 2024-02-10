##################### Extra Hard Starting Project ######################
import smtplib
import random
import datetime as dt
from pandas import pandas

MY_EMAIL = "toadenstartoad@gmail.com"
MY_PASSWORD = "uhijbidvecdjplgc"
NAME = ""

# ---------------- The letter reader ----------------------------

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt",
           "letter_templates/letter_4.txt"]
letter_chosen = random.choice(letters)
print(letter_chosen)

# ---------------- The time ----------------------------
now = dt.datetime.now()
month = now.month
day = now.day

print(month, day)

# ---------------- The data ----------------------------
data = pandas.read_csv("birthdays.csv", index_col=False)
data_dict = data.to_dict()

year_dict = data_dict["year"]
month_dict = data_dict["month"]
day_dict = data_dict["day"]
name_dict = data_dict["name"]

# ---------------- The for loop ----------------------------
for index, row in data.iterrows():
    row_month = row["month"]
    row_day = row["day"]
    NAME = row["name"]

    with open(letter_chosen, mode="r") as letter:
        birthday_letter = letter.read()
        birthday_letter = birthday_letter.replace("[NAME]", NAME)
        # print(birthday_letter)

    if month == row_month and day == row_day:
        EMAIL = row["email"]
        print(EMAIL)
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=f"{EMAIL}",
                msg=f"Subject:Happy Birthday!!!\n\n{birthday_letter}"
            )
            print("mail send")
