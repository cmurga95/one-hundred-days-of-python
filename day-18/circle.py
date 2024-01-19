from turtle import *
import random

tim = Turtle()
tim.shape('turtle')
tim.speed('slowest')
screen = Screen()
tim.color("blue", 'red')

screen.colormode(255)
tim.width(width=3)


def draw_shape(num_sides):
    angle = 360/_
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    randomcolor = [r,g,b]
    return randomcolor

def random_walk():
    angle = random.choice([0, 90, 180, 270])
    return angle

for _ in range(100):
    randomcolor = random_color()
    tim.pencolor(randomcolor)
    tim.circle(40)
    # screen.delay(10)
    current_heading = tim.heading()
    tim.setheading(current_heading+30)



screen.exitonclick()

