import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

letter_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

letter_dict = {row.letter: row.code for (index, row) in letter_data_frame.iterrows()}
print(letter_dict)
# {"A": "Alfa", "B": "Bravo"}

valid_code = True

while valid_code:
    word = input("Enter a word: ").upper()

    try:
        result = [letter_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only in the alphabet NOT IN THE BETABET!!!")
    else:
        print(result)
        valid_code = False


# Second Option "The real way🙃"

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [letter_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only in the alphabet NOT IN THE BETABET!!!")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()