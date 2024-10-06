from turtle import Turtle, Screen

dashed_turtle = Turtle()

dashed_turtle.shape("turtle")
dashed_turtle.color("brown")

for move in range(15):
    dashed_turtle.forward(10)
    dashed_turtle.penup()
    dashed_turtle.forward(10)
    dashed_turtle.pendown()

screen = Screen()
screen.exitonclick()
