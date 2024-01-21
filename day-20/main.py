from turtle import Screen, Turtle 
import time

from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkey(snake.up, key = "w")
screen.onkey(snake.left, key = "a")
screen.onkey(snake.right, key = "d")
screen.onkey(snake.down, key = "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.20)

    snake.move()


screen.exitonclick()