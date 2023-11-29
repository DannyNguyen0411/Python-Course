age = input("What is your current age?\n")

# input will always convert it to datatype 'string'
age_in_int = int(age)

years_remaining = 100 - age_in_int

days_remaning = years_remaining * 365
weeks_remaning = years_remaining * 52
months_remaning = years_remaining * 12

# check of the numbers are right
# print(months_remaning)

result = f"You have {days_remaning} days, {weeks_remaning} weeks, and {months_remaning} months remaining"
print(result)