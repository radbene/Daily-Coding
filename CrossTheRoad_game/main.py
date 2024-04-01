import score, cars, player
from turtle import Turtle, Screen
import random, time

#set up the screen and scoreboard
screen = Screen()
screen.colormode(1)
screen.setup(600,600)
screen.tracer(0)
t = player.Player()
scoreboard = score.Score()

screen.onkeypress(t.move_up,"Up")
screen.listen()



game = True
c = []      #list of cars
speed = 10  #speed of cars

while game:
    screen.update()
    if random.randint(1,6) == 1:
        c.append(cars.Car())    #create car approximately once every six loops
    for i in c:
        if i.xcor() < -330: #if car goes out of bounds then delete it
            c.pop(c.index(i))
        else:
            i.move(speed)
        if abs(t.xcor() - i.xcor()) < 35 and abs(t.ycor() - i.ycor()) <= 20:    #if turtle and car colide then it's game over
            game = False
            scoreboard.gg()
    if t.ycor() > 280:
        wait = True
        t.next_lvl()
        scoreboard.next_lvl()
        speed *= 1.5    #increase the speed of cars at each level
        time.sleep(1)
    time.sleep(0.15)

screen.exitonclick()