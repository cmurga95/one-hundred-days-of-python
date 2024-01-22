from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Score

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

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

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()