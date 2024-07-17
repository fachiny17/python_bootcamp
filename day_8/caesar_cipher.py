from alphabets_and_logo import alphabet

print("Welcome to Caesar Cipher!")

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("How may places do you want to shift?\n "))

if direction == 'encode':
    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")
        
    encrypt(plain_text=text, shift_amount=shift)
        
elif direction == 'decode':
    def decrypt(cipher_text, shift_amount):
        plain_text = ""
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter  = alphabet[new_position]
            plain_text += new_letter
        print(f"The decoded text is {plain_text}")
        
    decrypt(cipher_text=text, shift_amount=shift)
    
else:
    print("The direction you choose is invalid. Choose 'encode' or 'decode'.")