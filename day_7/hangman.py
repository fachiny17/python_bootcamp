import random
from hangman_words import word_list
from hangman_stages import stages



print("Welcome to HANGMAN!")
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
# print(f"The chosen word is {chosen_word}.")

display = []
for letter in chosen_word:
    display +="_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
          print(f"You've already guessed the {guess}.")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You loose a life.")    
      lives -= 1
      if lives ==0:
          end_of_game = True
          print(f"You loose! the word is {chosen_word}.")
        
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win!")
        
    print(stages[lives])