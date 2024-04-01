from turtle import Turtle

#I didn't know if saving highscore would work on other computers
#so I commented out the parts of the code that relate to it

#with open("/Users/Admin/Desktop/highscore.txt","r") as file:    #location of the file that stores the highscore
#    highscore = file.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hs = 0             #int(highscore)
        self.score = 0
        self.speed(0)
        self.goto(0,310)
        self.hideturtle()
        self.color("white")
        self.write(f"Score = {self.score}   Highscore = {self.hs}",False,"center",("Arial",24,"normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}   Highscore = {self.hs}",False,"center",("Arial",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over\nYour score was {self.score}   Highscore = {self.hs}",False,"center",("Arial",32,"normal"))
#        with open("/Users/Admin/Desktop/highscore.txt", "w") as file:
#           if self.score > self.hs:
#               self.hs = self.score
#           file.write(str(self.hs))