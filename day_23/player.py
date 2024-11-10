from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.forward(-MOVE_DISTANCE)

    def go_right(self):
        self.setx(self.xcor() + MOVE_DISTANCE)

    def go_left(self):
        self.setx(self.xcor() - MOVE_DISTANCE)
