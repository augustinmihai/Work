# Step 3:
    #create a separate file for the Ball Class in order to initialise the ball object

from turtle import Turtle

class Ball(Turtle):
#inherit the Turtle Class

    def __init__(self):
        super().__init__()
        self.color("white") #set colour to white
        self.shape("circle") #set the ball shape to circle
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


#create a move method to increment the ball initial movement
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        #increase speed everytime the ball hits a paddle
        self.move_speed * 0.9


    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()