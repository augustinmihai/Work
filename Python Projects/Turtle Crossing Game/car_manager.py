#Step 2 :
    #Create a separate file for defining the Car class behaviour

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

#Create the initialiser for the class
    def __init__(self):
        self.all_cars = [] #create a new empty list in order to get all the newly created cars
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):

        #create a random chance to generate to car, and only when the chance is equal to 1, create a car
        #because there are to many cars, we need to reduce the number of the cars
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square") #give the car a square shape
            new_car.shapesize(stretch_wid=1, stretch_len=2) #stretch car's shape
            new_car.penup() #lift up the pen
            new_car.color(random.choice(COLORS)) #give a random color from the colors list
            random_y = random.randint(-250, 250) #give  a random position on the y axis to fit the screen
            new_car.goto(300, random_y) #place the newly created car at the needed coordinates
            self.all_cars.append(new_car) #append the new car in the list of cars


    #create a function for moving the cars
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT





