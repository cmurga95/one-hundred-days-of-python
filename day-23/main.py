from turtle import Turtle, Screen
from crossing_turtle import main_character
from random_objects import CarManager
import time
from score import score
screen = Screen()
screen.screensize(600,600)
screen.title('Crossing turtle')
screen.bgcolor('black')
screen.tracer(0)

t = main_character()
car = CarManager()
levels = score()
game_on = True

robj = 5

screen.listen()
screen.onkey(t.go_up, "Up")

acc = 0
car.distance = Turtle.distance

while game_on:
    time.sleep(0.05)
    screen.update()

    car.create_car()
    car.move()

    for carz in car.all_cars:
        if carz.distance(t) < 20:
            game_on = False
            levels.game_over()

    if t.ycor() > 280:
        levels.levels()
        t.reset_position()
        car.car_speed += 5

screen.exitonclick()