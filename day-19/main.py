from turtle import Turtle, Screen

t = Turtle()

screen = Screen()

# functions as input 
def move_forward():
    t.forward(10)

def right():
    t.right(10)

def left():
    t.left(10)

def bw():
    t.back(0)

def res():
    t.reset()

def clear():
    t.clear()


screen.listen()

screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "a", fun = right)
screen.onkey(key = "d", fun = left)
screen.onkey(key = "s", fun = bw)
screen.onkey(key = "r", fun = res)
screen.onkey(key = "c", fun = clear)



screen.exitonclick()