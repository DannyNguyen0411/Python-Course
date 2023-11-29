# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_string = len(names)
randomizer = random.randint(0, num_string - 1)

person_who_will_pay = names[randomizer]

print(person_who_will_pay + " will pay for the dinner today")