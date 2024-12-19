import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
