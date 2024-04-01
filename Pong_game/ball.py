from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()

    def move(self):
        self.forward(0.3)   #speed of the ball

    def bounce_ver(self):   #reverse vertical movement direction
        self.setheading(-self.heading())
        self.move()
        
    def restart(self,n):    #place the ball in the middle and move it towards the player who last scored a goal
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.setheading(n * 180)

    def start(self):
        self.setheading(180)
        self.move()

#if the ball touches any of the paddles then bounce the ball
    def bounce_paddle1(self,pad):
        if pad <= self.ycor():
            self.setheading(abs(abs(pad) - abs(self.ycor())) * (60 / 70))
            self.move()
        else:
            self.setheading(-abs(abs(pad) - abs(self.ycor())) * 60 / 70)

    def bounce_paddle2(self,pad):
        if pad <= self.ycor():
            self.setheading(180 - abs(abs(pad) - abs(self.ycor())) * (60 / 70))
            self.move()
        else:
            self.setheading(180 + abs(abs(pad) - abs(self.ycor())) * 60 / 70)