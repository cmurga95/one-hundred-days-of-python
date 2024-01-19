import colorgram

colors = colorgram.extract('img1.jpg', 20)

colorsList = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    colorsList.append(new_color)

from turtle import *
import random

t = Turtle()

screen = Screen()
screen.colormode(255)

def pick_random_color(color):
    return random.choice(color)



tp = t.pos()
print(tp)

t.penup()
t.setposition(-350,-350)
x,y = t.pos()

def drawPoints():
    color = pick_random_color(colorsList)
    t.dot(20, color)
    t.penup()
    t.forward(50)

def reset():
    t.penup()
    x,y = t.pos()
    t.setx(-350)
    t.sety(y+50)

for i in range(15):
    for _ in range(15):
        drawPoints()
    reset()



screen.exitonclick()

