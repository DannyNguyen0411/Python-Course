# You have to use the close keyword so it will close the file.
file = open("my_file.txt")
contenter = file.read()
print(contenter)
file.close()

# Don't have to close it, because the key words will do it for you
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Edit text by using write by overwriting the file
with open("new_file.txt", mode="w") as file:
    file.write("New MotherFucking Text!")

# Append text and write that in the file
while True:
    with open("new_file.txt", mode="a") as file:
        file.write("\nNew MotherFucking Text!")

# There are 3 modes: r, w and a
