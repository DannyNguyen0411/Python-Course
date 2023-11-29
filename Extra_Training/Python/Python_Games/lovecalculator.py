# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name_of_counting = name1.lower() + name2.lower()

# True
name_counter_T = name_of_counting.count('t')
name_counter_R = name_of_counting.count('r')
name_counter_U = name_of_counting.count('u')
name_counter_E = name_of_counting.count('e')

name_counter_true = name_counter_T + name_counter_R + name_counter_U + name_counter_E

# Love
name_counter_L = name_of_counting.count('l')
name_counter_O = name_of_counting.count('o')
name_counter_V = name_of_counting.count('v')
name_counter_E = name_of_counting.count('e')

name_counter_love = name_counter_L + name_counter_O + name_counter_V + name_counter_E

result = int(str(name_counter_true) + str(name_counter_love))

if result <= 10 or result >= 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")



