# List Comprehension Compare it with the for loop
numbers = [1, 2, 3]
# Key word for the list Comprehension
# new_list = [new_item = for item in list]

new_list = [n + 1 for n in numbers]
print(new_list)

# List + For loop
numbers = [1, 2, 3]
new_number_list = []
for n in numbers:
    add_1 = n + 1
    new_number_list.append(add_1)
print(new_number_list)

# Can also work with the string
name = "Angela"
new_list_letter = [letter for letter in name]
print(new_list_letter)

# Created a range list by multiply it by 2
list_range = [n * 2 for n in range(1, 5)]
print(list_range)

# Create a new keyword with a 'if' statement
# new_list = [new_item for item in list if test]
names = ["Alex", "Clover", "Sam", "Jerry", "Mandy", "WOOHPS"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [n.upper() for n in names if len(n) > 5]
print(long_names)


# Tried something of the project for day 26
the_list = []

for n in new_list_letter:
    if n == "A" or n == "a":
        # print("Alpha")
        the_list.append("Alpha")
    elif n == "N" or n == "n":
        # print("Nintendo")
        the_list.append("Nintendo")
    elif n == "G" or n == "g":
        # print("Gray")
        the_list.append("Gray")
    elif n == "L" or n == "l":
        # print("Lol")
        the_list.append("Lol")
    elif n == "E" or n == "e":
        # print("Egg")
        the_list.append("Egg")
    else:
        print("test")

print(the_list)

# Conclusion,
# List comprehenssions is the for loop, but a in one line of code.