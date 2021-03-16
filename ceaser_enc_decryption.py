#this is a basic ceaser encryption code
import string 

text=input("input a text here: ")
ceaser_shift=5

my_alphabet=string.ascii_letters
shift=my_alphabet[ceaser_shift:]+ my_alphabet[:ceaser_shift]

table= str.maketrans(my_alphabet, shift)

encryption= text.translate(table)

print(encryption)

#decryption
def decrypt():
    
    print("-------Ceaser decryption------")
    encrypted_message = input("Enter the encrypted message ").strip()
    print()
    key = int(input("Enter the shift key: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in my_alphabet:
            position = my_alphabet.find(c)
            new_position = (position - key) % 26
            new_character = my_alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    print("Your decrypted message is:\n")
    print(decrypted_message)

decrypt()
