from turtle import Turtle


class setup_paddle(Turtle):

    def __init__(self, X, Y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(X, Y)
        self.shapesize(stretch_wid = 5, stretch_len = 1)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(), new_y)
    