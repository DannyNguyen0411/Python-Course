import random

name_string = input("Give me everybody's names, separated by a comma. ")
names = name_string.split(", ")

num_items = len(names)

randomizer = random.randint(0, names - 1)
will_pay = names[num_items]

print(f"{will_pay}, is going to pay for the diner")