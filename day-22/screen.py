from turtle import Turtle, Screen

class setup_screen:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)
        self.screen.exitonclick()
        self.screen.title('Pong')