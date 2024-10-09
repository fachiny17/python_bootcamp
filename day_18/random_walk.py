# from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(15)  # pensize is same as width
tim.speed("fastest")

for move in range(300):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random_color())

screen = t.Screen()
screen.exitonclick()
