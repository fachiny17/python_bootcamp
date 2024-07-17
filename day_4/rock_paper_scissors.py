import random

rock = '''ROCK'''
paper = '''PAPER'''
scissors = '''SCISSORS'''

game_objects = [rock, paper, scissors]

user_input = int(input("What do you choose? (Type 0 for Rock, 1 for Paper or 2 for Scissors) "))
if user_input >= 3 or user_input < 0:
    print("You type an invalid number, you loose!")
else:
    print(game_objects[user_input])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {computer_choice} which is {game_objects[computer_choice]}")

    if user_input ==0 and computer_choice==2:
        print("You win!")
    elif user_input ==2 and computer_choice==0:
        print("You loose!")
    elif user_input < computer_choice:
        print("You loose!")
    elif user_input > computer_choice:
        print("You win!")
    elif computer_choice==user_input:
        print("It's a draw!")