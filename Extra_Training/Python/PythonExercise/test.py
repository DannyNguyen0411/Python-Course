print("Welcome to the yolo counter!")
name = input("What is your name?\n")
age = int(input("What is your age?\n"))
year = int(input("What for year are you born?\n"))

result = print(f"Your name is {name}. You are {age} right know. You are born in the year {year}.")

age_in_weeks = 100 - age

days_remaining = age_in_weeks * 365
weeks_remaining = age_in_weeks * 52
months_remaining = age_in_weeks * 12

input("If you life till 100 years, What are you last words?\n")

true_result = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months remaining"

print(true_result)
print("Safe those words for later😉")
