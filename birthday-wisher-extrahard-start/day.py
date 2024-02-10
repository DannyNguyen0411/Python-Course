import datetime as dt

now = dt.datetime.now()
current_time = now.today()
print(current_time)

month = now.month
print(month)

day = now.day
print(day)

if month in current_time:
    print("Day!!!")
else:
    print("Fuck!!!!")
