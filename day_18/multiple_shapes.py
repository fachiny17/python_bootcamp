# TODO:
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon.
# Each of the shapes should have a random colour and each side should be 100 in terms of lenght

from turtle import Turtle, Screen

multi = Turtle()

multi.shape("turtle")

for triangle in range(3):
    multi.color("brown")
    multi.right(120)
    multi.forward(100)

for square in range(4):
    multi.color("yellow")
    multi.right(90)
    multi.forward(100)

for pentagon in range(5):
    multi.color("green")
    multi.right(72)
    multi.forward(100)

for hexagon in range(6):
    multi.color("red")
    multi.right(60)
    multi.forward(100)

for heptagon in range(7):
    multi.color("black")
    multi.right(51.43)
    multi.forward(100)

for octagon in range(8):
    multi.color("pink")
    multi.right(45)
    multi.forward(100)

for nonagon in range(9):
    multi.color("purple")
    multi.right(40)
    multi.forward(100)

for decagon in range(10):
    multi.color("indigo")
    multi.right(36)
    multi.forward(100)

screen = Screen()
screen.exitonclick()

# Excellently done. Congrats! for doing this yourself

# ------------------------------------------------------------------------------------------------------------------
# Professional approach

# import turtle as t
# import random
#
# tim = t.Turtle()
#
# colours = ["red","brown","black","orange","green","indigo"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for move in range(num_sides):
#         tim.forward(100) 
#         tim.right(angle) 
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)
