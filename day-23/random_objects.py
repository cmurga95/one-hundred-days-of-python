from turtle import Turtle, Screen
import random

X = 330
Y = random.randint(0,300)


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def starting_position(self):
        x = random.choice([-300,300])
        y = random.randint(-300,300)
        self.goto(x,y)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_car(self):
        random_chance = random.randint(1,10)
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        if random_chance == 1:
            self.new_car = Turtle("square")
            self.new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            self.new_car.penup()
            self.new_car.color((R,G,B))
            random_y = random.randint(-250,250)
            self.new_car.goto(300,random_y)
            self.all_cars.append(self.new_car)