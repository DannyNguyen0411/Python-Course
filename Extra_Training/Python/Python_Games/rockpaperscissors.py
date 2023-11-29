import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
weapons = [rock, paper, scissors]
num_string = len(weapons)

user_action = input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors\n")

if user_action == "0":
    print(rock)
elif user_action == "1":
    print(paper)
elif user_action == "2":
    print(scissors)

computer_action = random.randint(0, num_string - 1)

print(weapons[computer_action])

