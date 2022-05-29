# # Step 2:
# # Create a separate file with the "Paddle Class" in order to initialise new paddle objects that
# # can be used whenever we want

from turtle import Turtle


class Paddle(Turtle):
#inherit the Turtle class

    def __init__(self, position):
        super().__init__()
        self.shape("square")  # give it a square shape
        self.color("white")  # give it the colour white
        self.shapesize(stretch_wid=5, stretch_len=1)  # set the stretch width and length
        self.penup()  # use .penup() method in order not to leave trails on the screen
        self.goto(position)  # Place the paddle at the needed coordinates


    # create a function for the "UP" movement
    def go_up(self):
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    # create a function for the "DOWN" movement
    def go_down(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
