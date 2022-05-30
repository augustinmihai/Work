#Step 1:
    #Create a separate file for the player class.
    #The player will be a turtle shape

from turtle import Turtle
#import Turtle class

STARTING_POSITION = (0, -280)  #Create a starting position
MOVE_DISTANCE = 10  #Create a move_distance
FINISH_LINE_Y = 280 #create finish line point


class Player(Turtle):
#inherit the Turtle class

#create and overwrite the initialiser
    def __init__(self):
        super().__init__()
        self.shape("turtle") #give the player, the turtle shape
        self.penup() #lift up the "pen"
        self.go_to_start()
        self.setheading(90) #set the heading to be looking to the  north point

#create a function for moving the turtle
    def go_up(self):
        self.forward(MOVE_DISTANCE)

#create a function for placing the turtle player at the starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)

#create a function to check if the player has reached finish line
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


