from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("white")

    def update_score(self):
        self.score += 1
        self.clear()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", align="center", font=("Arial", 15, "bold"))

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over ", align="center", font=("Arial", 20, "bold"))








