from turtle import Turtle, Screen

turtle_square = Turtle()

turtle_square.shape("turtle")
turtle_square.color("brown")

# turtle_square.forward(100)
# turtle_square.right(90)
# turtle_square.forward(100)
# turtle_square.right(90)
# turtle_square.forward(100)
# turtle_square.right(90)
# turtle_square.forward(100)

for move in range(1000):
    turtle_square.forward(100)
    turtle_square.right(90)

screen = Screen()
screen.exitonclick()
