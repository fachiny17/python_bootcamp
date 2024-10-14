from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# def move_forward():
#    tim.forward(10)

def movement(move_forward, move_backward):
    move_forward = tim.forward(10)
    move_backward = tim.backward(10)


movement(move_forward=10, move_backward=10)

screen.listen()()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="w", fun=move_backward)
screen.exitonclick()
