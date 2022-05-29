# Step 1:
    #Create a screen background for the Pong Game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen() # Create a new screen
screen.bgcolor("black") #set background colour to black
screen.setup(width=800, height=600) # set the screen dimensions
screen.title("Pong") #set screen title to Pong
screen.tracer(0)

r_paddle = Paddle((350, 0)) #initialise the right paddle
l_paddle = Paddle((-350, 0)) #initialise the left paddle
ball = Ball() #initialise the ball object
score = Scoreboard()


#Make the screen to listen to the user inputs/buttons
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

#create a while loop for the game to run in it
while game_is_on:

    #delay by a time of 0.1s the screen in order to clearly see the ball moving
    time.sleep(ball.move_speed)
    #update screen
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #the ball needs to bounce on y axis
        ball.bounce_y()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        #the ball needs to bounce on the x axis
        ball.bounce_x()


    #Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #Detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick() # make the screen exit on click