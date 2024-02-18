from turtle import Turtle, Screen

tom = Turtle()


def move_forward():
  tom.forward(10)

def move_backward():
  tom.backward(10)

def move_clockwise():
  tom.right(10)

def move_counter_clockwise():
  tom.left(10)

def clear_everything():
  tom.reset()


screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=move_counter_clockwise, key='a')
screen.onkey(fun=move_clockwise, key='d')
screen.onkey(fun=clear_everything, key='c')
screen.exitonclick()