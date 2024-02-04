import smtplib

my_email = "toadenstartoad@gmail.com"
password = "uhijbidvecdjplgc"
# my_email = "dda.nguyen1@gmail.com"
# password = "skscuffqchkjkhxb"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="dda.nguyen1@gmail.com",
        msg="Subject:Hello!\n\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n\nKind regards, "
            "\n\nDanny Duy-Anh Nguyen"
    )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# day = now.day
# print(day_of_week)
#
# # if year == 2024 and month == 2 and day == 4:
# #     print("Happy Birthday Lilian!")
# # else:
# #     print("9/11 is coming for you!")
#
# date_of_birth = dt.datetime(year=2001, month=9, day=11, hour=9, minute=3)
# print(date_of_birth)