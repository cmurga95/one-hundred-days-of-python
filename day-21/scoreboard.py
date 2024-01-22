from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 16, "normal")
X,Y = (0 ,250)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x = X, y = Y)
        self.color('white')
        self.score_number = 0
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score_number}', align = ALIGNMENT, font = FONT)


    def add_score(self):
        self.score_number += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align = ALIGNMENT, font = FONT)
       