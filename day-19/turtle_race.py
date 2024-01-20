from turtle import *
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 350) 
user_bet = screen.textinput(title = 'make your bet', prompt = 'Which turtle will win the race? Enter a color: ')
print(user_bet)

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
y_pos = [-150, -100, -50, 0, 50, 100]
all_turtles = []

for t_i in range(0, 6):
    new_turtle = Turtle(shape = 'turtle')
    new_turtle.color(colors[t_i])
    new_turtle.penup()
    new_turtle.shape('turtle')
    new_turtle.goto(x = -230, y = y_pos[t_i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                is_race_on = False
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()