from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def move_up(self):
        self.forward(8)

    def next_lvl(self):
        self.goto(0,-280)