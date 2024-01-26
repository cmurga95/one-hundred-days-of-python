from turtle import Screen
from paddle import setup_paddle
from ball import ball
from score import score
import time

screen = Screen()
screen.title('Pong')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = setup_paddle(350, 0)
l_paddle = setup_paddle(-350, 0)

bball = ball()

sccore = score()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True

while game_on:
    time.sleep(0.05)
    screen.update()
    bball.move()
    #detect colission
    if bball.ycor() > 270 or bball.ycor() < -270:
        #bounce
        bball.bounce()
    
    #detect collision with right paddle
    if bball.distance(r_paddle) < 70 and bball.xcor() > 320:
        bball.paddle_bounce()

    if bball.xcor() > 350:
        bball.reset_position()
        sccore.l_point()

    if bball.distance(l_paddle) < 70 and bball.xcor() < -320:
        bball.paddle_bounce()

    if bball.xcor() < -350:
        bball.reset_position()
        sccore.r_point()
    


screen.exitonclick()