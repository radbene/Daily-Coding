from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()

    def declare(self):
        self.write(f"{self.score}",False,"center",("Arial",48,"normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}",False,"center",("Arial",48,"normal"))
        