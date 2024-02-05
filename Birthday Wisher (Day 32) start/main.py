import smtplib
import datetime as dt
from random import choice

my_email = "toadenstartoad@gmail.com"
password = "uhijbidvecdjplgc"
# my_email = "dda.nguyen1@gmail.com"
# password = "skscuffqchkjkhxb"

# --------------------------- Setup Mail ------------------------------------
with open(file='quotes.txt') as data:
    list_of_quotes = data.readlines()
    quote_of_today = choice(list_of_quotes)
    # print(f"{quote_of_today}")


# Datetime
now = dt.datetime.now()
day_of_week = now.weekday()
week_of_now = now.weekday()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if day_of_week == week_of_now:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="dannyduyanhnguyen@outlook.com, dda.nguyen1@gmail.com",
            msg=f"Subject:Quotes of today!\n\n{quote_of_today}\n\nKind regards,\n\n"
                "\n\nDanny Duy-Anh Nguyen"
        )
        print("Mail sended")
    else:
        print(f"The quote of today: {quote_of_today}")
    # connection.login(user=my_email, password=password)
    # connection.sendmail(
    #     from_addr=my_email,
    #     to_addrs="dannyduyanhnguyen@outlook.com",
    #     msg=f"Subject:Quotes of today!\n\n{quote_of_today}\n\nKind regards,\n\n"
    #         "\n\nDanny Duy-Anh Nguyen"
    # )

# to_addrs="thientrinhnguyen@ziggo.nl, maianh.maryann@gmail.com, dannyduyanhnguyen@outlook.com"


year = now.year
month = now.month
day = now.day

print(week_of_now)




# my_birthday = dt.datetime(year=2004, month=11, day=4, hour=10, minute=3)
# print(my_birthday)
#
# if year == 2024 and month == 2 and day == 4:
#     print("Happy Birthday Lilian!")
# else:
#     print("9/11 is coming for you!")
#
# date_of_birth = dt.datetime(year=2001, month=9, day=11, hour=9, minute=3)
# print(date_of_birth)

