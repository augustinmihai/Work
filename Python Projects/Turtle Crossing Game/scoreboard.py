#Step 3:
    #Create a separate file for the ScoreBoard class

from turtle import  Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
#inherit the Turtle class
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    #create a new function for updating the scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    #keep track and increase the current level
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        #update the scoreboard to the new level

    def game_over(self):
        #if the game is over, make the scoreboard go to the center position and write game over
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

