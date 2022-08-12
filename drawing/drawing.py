from turtle import Turtle, Screen

tim = Turtle()

my_screen = Screen()
my_screen.listen()

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def head_set_left():
    tim.left(10)

def head_set_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()

my_screen.onkey(key="f", fun=move_forwards)
my_screen.onkey(key="b", fun=move_backward)
my_screen.onkey(key="l", fun=head_set_left)
my_screen.onkey(key="r", fun=head_set_right)
my_screen.onkey(key="c", fun=clear)

my_screen.exitonclick()
