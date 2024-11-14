import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross Road Game")
screen.tracer(0)


def play_game():
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

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_down, "Down")
    screen.onkey(player.go_right, "Right")
    screen.onkey(player.go_left, "Left")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        # Detect when turtle collides with car
        for car in car_manager.all_cars:
            if car.distance(player) < 18:
                scoreboard.game_over()
                game_is_on = False
                play_again(screen)

        # Detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_score()

    screen.exitonclick()


def play_again(self, screen):
    again_choice = screen.textinput(
        title="Play Again", prompt="Do you want to play again? (yes/no)").lower()
    if again_choice == "yes":
        screen.reset()
        self.hideturtle()
        play_game()
    else:
        print("Thank you for playing!")
        screen.bye()


play_game()
