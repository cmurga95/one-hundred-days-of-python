from turtle import Turtle

class score(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.level = 1
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 300)
        self.write(f"Level: {self.level}", align = "center", font = ("Courier", 20, "normal"))

    def levels(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align = "center", font = ("Courier", 30, "normal"))
