from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

class main_character(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0,-280)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def reset_position(self):
        self.goto(0,-280)