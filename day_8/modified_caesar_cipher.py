from alphabets_and_logo import alphabet

def caesar(start_text, shift_amount, cipher_direction):
    end_text =""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        