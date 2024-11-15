import yt_dlp
from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


def play_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    options = ["yes", "no"]
    user_choice = None

    # Function to get user choice

    def get_user_choice():
        return screen.textinput(title="Make your choice", prompt="Do you want to start the game? (yes/no): ").lower()

    # Main logic to handle user input
    while user_choice not in options:
        user_choice = get_user_choice()

        if user_choice not in options:
            print(f"Invalid option, please input either {', '.join(options)}.")

        if user_choice == "no":
            print("Quitting Game!")
            screen.bye()

    # If the user chose "yes", initialize game elements
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False
            # scoreboard.game_over()
            play_again(screen)

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
                # game_is_on = False
                # scoreboard.game_over()
                play_again(screen)

    screen.exitonclick()


def play_again(screen):
    again_choice = screen.textinput(
        title="Play Again", prompt="Do you want to play again? (yes/no)").lower()
    if again_choice == "yes":
        screen.clear()
        screen.tracer(0)
        play_game()
    elif again_choice == 'no':
        print("Thank you for playing!")
        screen.bye()
    else:
        print("Invalid choice. Exiting the game")
        screen.bye()


play_game()
