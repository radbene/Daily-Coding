import turtle as t
import random as r

class Fruit:
    def __init__(self):
        self.create_fruit()
        self.position_x = round(self.f.xcor())
        self.position_y = round(self.f.ycor())

    def create_fruit(self):
        self.f = t.Turtle("circle")
        self.f.color("blue")
        self.f.penup()
        self.f.goto(r.randint(-14, 14) * 20, r.randint(-14, 14) * 20)
    def hide(self):
        self.f.hideturtle()