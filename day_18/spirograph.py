import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colo = (r, g, b)
    return rand_colo


def draw_spirograph(size_of_gap):
    for move in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)


draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()
