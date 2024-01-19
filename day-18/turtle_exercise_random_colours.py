from turtle import *
import random

tim = Turtle()
tim.shape('turtle')

screen = Screen()
tim.color("blue", 'red')

screen.colormode(255)

def draw_shape(num_sides):
    angle = 360/_
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for _ in range(3,100):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.pencolor(r,g,b)
    draw_shape(_)



screen.exitonclick()

