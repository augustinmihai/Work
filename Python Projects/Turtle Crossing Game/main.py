###############################################################
##           THE TURTLE CROSSING STREET GAME                 ##
##     PURPOSE OF THE GAME IS TO CROSS THE STREET WITHOUT    ##
##                 GETTING HIT BY THE CARS                   ##
###################### ARE YOU READY ?!########################

import time
#import and use the time module for updating the screen

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()  #create a new screen
screen.setup(width=600, height=600) #set up screen dimensions
screen.tracer(0)

player = Player()
#create a new player from the player class


#create a new car_manager object to handle the cars
car_manager = CarManager()


#create a new scoreboard object for displaying the current score
scoreboard = Scoreboard()


#make the screen "listen" for the Up command , in order to move the turtle up the screen
screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
#create a while loop for the game, in order to run it

while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create new cars and make the move
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with the cars
    for car in car_manager.all_cars:
        #if the distance between the car and the player is less than 20, stop the game
        if car.distance(player) < 20:
            game_is_on = False
            #if the game is over, wrtite game over on the center of the screen
            scoreboard.game_over()

    #Detect a succesfull crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
