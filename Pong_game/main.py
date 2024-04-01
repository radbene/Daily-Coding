from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from turtle import Turtle, Screen
import time

def restart(i):     #if one of the players scores then respawn ball and move it in his direction
    paddle1.goto(-345, 0)
    paddle2.goto(345, 0)
    ball.restart(i)
    time.sleep(1.5)
def boundry():  #creates borders
    bound = Turtle()
    bound.penup()
    bound.color("white")
    bound.hideturtle()
    bound.goto(300, 300)
    bound.pendown()
    bound.goto(-300, 300)
    bound.goto(-300, -300)
    bound.goto(300, -300)
    bound.goto(300, 300)
    return None

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)

print(screen.window_width(),screen.window_height())
screen.tracer(n = 0)
boundry()

#setting up the paddles
paddle1 = Paddle()
paddle2 = Paddle()
paddle1.goto(-345, 0)
paddle2.goto(345, 0)

ball = Ball()

#setting up the scoreboard
scoreboard1 = Scoreboard()
scoreboard1.goto(-150, 230)
scoreboard1.declare()
scoreboard2 = Scoreboard()
scoreboard2.goto(150, 230)
scoreboard2.declare()



game = True
#left paddle moves up with 'w' and down with 's'
screen.onkeypress(paddle1.move_up, "w")
screen.onkeypress(paddle1.move_down, "s")

#right paddle moves up with 'o' and down with 'l'
screen.onkeypress(paddle2.move_up, "o")
screen.onkeypress(paddle2.move_down, "l")
screen.listen()

ball.start()

while game:
    ball.move()
    #check if ball touches any of the paddles
    if abs(round(ball.xcor() - paddle1.xcor())) == 70 and abs(round(ball.ycor() - paddle1.ycor())) < 70:
        ball.bounce_paddle1(paddle1.ycor())
    if abs(round(ball.xcor() - paddle2.xcor())) == 70 and abs(round(ball.ycor() - paddle2.ycor())) < 70:
        ball.bounce_paddle2(paddle2.ycor())
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce_ver()
    #check if any of the players scored
    if ball.xcor() > 300:
        scoreboard1.update_score()
        restart(1)
    if ball.xcor() < -300:
        scoreboard2.update_score()
        restart(2)

    screen.update()
    if scoreboard1.score == 5 or scoreboard2.score == 5:
        game = False
    #game ends if one of the players reaches 5 points

end_text = Turtle()
end_text.hideturtle()
end_text.color("white")
end_text.write("GG",False,"center",("Arial",80,"normal"))


screen.exitonclick()