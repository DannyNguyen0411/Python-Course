PLACEHOLDER = "[name]"

#TODO: Create a letter using starting_letter.txt
with open("input/Letters/starting_letter.txt") as letter:
    invitation = letter.read()
    print(invitation)

#for each name in invited_names.txt
with open("input/Names/invited_names.txt") as name:
    names = name.readlines()
    print(names)
    for stripper in names:
        stripped_name = stripper.strip()
        # Replace the [name] placeholder with the actual name.
        letter = invitation.replace(PLACEHOLDER, stripped_name)
        print(f"{letter}")
        # #Save the letters in the folder "ReadyToSend".
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(letter)



# # 👇Answer
# PLACEHOLDER = "[name]"
#
# with open("./input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         print(new_letter)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)




    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp