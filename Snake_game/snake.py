import turtle as t

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.position_x = [0,-20,-40]
        self.position_y = [0,0,0]

    def create_snake(self):
        positions = [(0, 0), (-20, 0), (-40, 0)]    #starting positions
        for pos in positions:
            new_segment = t.Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.snake.append(new_segment)


    def move(self):
        #function has to check if any segment is out of bounds before and after moving
        #because snake is teleporting segment by segment and only checking if any segment is out of bounds after moving
        #would seperate the snake
        returning_val = True
        for i in range(len(self.snake) - 1, 0, -1): #each segment goes in place of the next segment
            self.snake[i].goto(self.snake[i - 1].position())
            self.position_x[i] = round(self.snake[i].xcor())
            if self.position_x[i] <= -300 or self.position_x[i] >= 300: #if out of bounds  then teleport to the other side
                self.position_x[i] = self.position_x[i] * (-1) + round(self.position_x[i] / 300) *20
                self.snake[i].goto(self.position_x[i],self.position_y[i])
            self.position_y[i] = round(self.snake[i].ycor())
            if self.position_y[i] <= -300 or self.position_y[i] >= 300:
                self.position_y[i] = self.position_y[i] * (-1) + round(self.position_y[i] / 300) *20
                self.snake[i].goto(self.position_x[i], self.position_y[i])

        self.snake[0].forward(20)   #move the head
        self.position_x[0] = round(self.snake[0].xcor())

        if self.position_x[0] <= -300 or self.position_x[0] >= 300: #again check if out of bounds
            self.position_x[0] = self.position_x[0] * (-1) + round(self.position_x[0] / 300) *20
            self.snake[0].goto(self.position_x[0], self.position_y[0])
            returning_val = False

        self.position_y[0] = round(self.snake[0].ycor())

        if self.position_y[0] <= -300 or self.position_y[0] >= 300:
            self.position_y[0] = self.position_y[0] * (-1) + round(self.position_y[0] / 300) *20
            self.snake[0].goto(self.position_x[0], self.position_y[0])
            returning_val = False

        return returning_val
#returning_val is boolean which tells if any of the segments of the snake hit the wall(The game ends on hard mode)



    def add_segment(self):
        pos = self.snake[len(self.snake)-1].position()
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.snake.append(new_segment)
        self.position_x.append(pos[0])
        self.position_y.append(pos[1])
