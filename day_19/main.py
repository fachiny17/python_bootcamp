from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
# setup set the size and position of the main window. the width=500 and height=400
screen.setup(width=500, height=400)

user_choice = screen.textinput(
    title="Make your choice", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


y_positions = [-120, -70, -20, 20, 70, 120]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    if user_choice not in colors:
        print("Invalid color, please colors should be among "+", ".join(colors))
        is_race_on = False
    else:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_choice:
                    print(f"You've won! The {
                          winning_color} turtle is the winner.")
                else:
                    print(f"You've lost! The {
                          winning_color} turtle is the winner.")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
