alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Do you want to 'encode' or to decode?\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Works if the 
def encrypt(plain_text, shift_amount):

    clipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        clipher_text += new_letter
    print(clipher_text)

def decrypt(clipher_text, shift_amount):
    plain_text = ""
    for letter in clipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(plain_text)
    

if direction == "encode":
    encrypt(plain_text= text, shift_amount= shift)
elif direction == "decode":
    decrypt(clipher_text= text, shift_amount= shift)
else:
  letter = input("Because you haven't chose 'encode' or 'decode', which letter do you guess?\n")
  random_letter = random.choice(alphabet)
  print(f"The letter is '{random_letter}' and you chose '{letter}'")
  if random_letter == letter:
    print("You Win!")
  else:
    print("You Lose -_- , try again!")