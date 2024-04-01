from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-200,250)
        self.write(f"Level: {self.lvl}",False,"center",("Arial",30,"normal"))

    def next_lvl(self):
        self.lvl += 1
        self.clear()
        self.write(f"Level: {self.lvl}",False,"center",("Arial",30,"normal"))

    def gg(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GG \nYour level was {self.lvl}", False, "center", ("Arial", 60, "normal"))

