from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(6)
        self.penup()


    def move_up(self):
        #if self.ycor() > -250 and self.ycor() < 250:
            self.setheading(90)
            self.forward(5)

    def move_down(self):
        #if self.ycor() > -250 and self.ycor() < 250:
            self.setheading(270)
            self.forward(5)