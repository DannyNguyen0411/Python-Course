import smtplib
import datetime as dt
import schedule
from random import choice

MY_EMAIL = "toadenstartoad@gmail.com"
MY_PASSWORD = "uhijbidvecdjplgc"

# --------------------------- Setup Mail ------------------------------------

# Creating a list of random quotes
with open(file='quotes.txt') as data:
    list_of_quotes = data.readlines()
    quote_of_today = choice(list_of_quotes)
    # print(f"{quote_of_today}")


def send_quote():
    # Datetime
    now = dt.datetime.now()
    week_of_now = now.weekday()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        if week_of_now == 1:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="dannyduyanhnguyen@outlook.com, dda.nguyen1@gmail.com",
                msg=f"Subject:The quote of Today!\n\n{quote_of_today}\n\nKind regards,\n\n"
                    "\n\nDanny Duy-Anh Nguyen"
            )
            print("Mail sended")
        else:
            print(f"No mail will be send!\nThe quote of today: {quote_of_today}")


# Schedule the job to run every Monday at a specific time
schedule.every().monday.at("16:58").do(send_quote)

# Run pending tasks indefinitely
while True:
    schedule.run_pending()