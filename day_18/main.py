# turtle documentation can be found in docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen

timmy_turtle = Turtle()


timmy_turtle.shape("turtle")
timmy_turtle.color("brown")
timmy_turtle.forward(100)
timmy_turtle.right(90)


screen = Screen()
screen.exitonclick()
