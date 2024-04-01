import turtle as t
import time
import snake
import fruit
import scoreboard

#Easy game mode allows you to go through walls

#Setting up the screen and mode
screen = t.Screen()
screen.tracer(n = 0)
screen.screensize(600,600)
screen.bgcolor("black")
screen.title("Snake GAME")
dif = screen.numinput("Difficulty","Easy - 0\nHard - 1",0,0,1)

bound = t.Turtle()
bound.hideturtle()
bound.color("white")
bound.penup()
#Setting up the walls
bound.goto(-300,-300)
bound.pendown()
bound.goto(-300,300)
bound.goto(300,300)
bound.goto(300,-300)
bound.goto(-300,-300)

#Setting up the snake and scoreboard
snake = snake.Snake()
game_is_on = True
score = scoreboard.Scoreboard()
screen.update()

#move functions(No turnarounds)
def up():
    if snake.snake[0].heading() != 270:
        snake.snake[0].setheading(90)
def right():
    if snake.snake[0].heading() != 180:
        snake.snake[0].setheading(0)
def down():
    if snake.snake[0].heading() != 90:
        snake.snake[0].setheading(270)
def left():
    if snake.snake[0].heading() != 0:
        snake.snake[0].setheading(180)

screen.onkeypress(key="w", fun=up)
screen.onkeypress(key="d", fun=right)
screen.onkeypress(key="s", fun=down)
screen.onkeypress(key="a", fun=left)
screen.listen()
f = fruit.Fruit()
fruit_exists = True


while game_is_on:
    time.sleep(0.1) #Delay between each frame
    if not fruit_exists:    #if there is no fruit then spawn one
        f = fruit.Fruit()
        fruit_exists = True

    if f.position_x == snake.position_x[0] and f.position_y == snake.position_y[0]: #check if Snake has eaten the fruit
        score.add_score()
        fruit_exists = False
        f.hide()
        snake.add_segment()
        screen.update()
        del f
    screen.update()
    if dif == 1:
        game_is_on = snake.move()
    else:
        snake.move()
    for i in range(1,len(snake.snake)): #check if none of the snake segments are colliding
        if snake.position_x[0] == snake.position_x[i] and snake.position_y[0] == snake.position_y[i]:
            game_is_on = False

score.game_over()
screen.exitonclick()
