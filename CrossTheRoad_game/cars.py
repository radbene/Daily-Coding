from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.pos = (random.randint(280, 650), random.randint(-250, 270))    #spawn cars on the right behind the screen
        self.penup()
        self.speed("fastest")
        self.goto(self.pos)
        self.color(random.randint(10,255)/255,random.randint(10,255)/255,random.randint(10,255)/255) #random color (not white)
        self.shape("square")
        self.shapesize(1,3,1)
        self.setheading(180)

    def move(self,s):
        self.forward(s)

    def next_lvl(self):
        self.goto(self.pos)