# random_walk.py

# Programming Project #5: Random Walk
# A program that uses a pseudo random number generator to draw a
# random walk line.
# CS-1400-X01, Due July 15, 2018

# Original Problem: Draw a line using a pseudo random number generator.

# Major Steps and Points of Solution:

#   - A major step was breaking down the general problem into smaller problems.

#   - The smaller problems included:

#      1. Accepting user input, and validating it with a while-True function
#         with try and except.
#      2. Determining what the program needed to return (a straight distance
#         value, an actual distance value, and a graph with the line drawn).
#      3. Creating the window for the line to be drawn in.
#      4. Writing the formula to calculate the straight distance and actual
#         distance.
#      5. Encapsulating variables and methods in a class.

#   - The program utilizes the class the_GUI, which consists of four functions:
#     __init__(), draw_graph(), draw_random_walk(), and print_results().

#   - The program also consists of a main() function.

#   - Uses a pseudo random number generator to draw a line.

#   - The random direction generator uses three equations:
#      1. angle = random() * 2 * math.pi
#      2. x = x + cos(angle)
#      3. y = y + sin(angle)

# What I Learned:

#   - I used a top-down approach to break the general problem into smaller
#     problems, and then used spiral design techniques and testing to test
#     my program as I added new lines of code.

#   - The beginning and the end were the most difficult parts for me.

#   - In the beginning, as I was determining what my program needed to do, I
#     began writing out the objectives and attributes that my program needed to
#     have and perform. From there I was able to split the general problem
#     into smaller problems.

#   - The end was when I made the class the_GUI. It was difficult because I
#     have not had much experience with classes, but I learned a lot from
#     making and utilizing a class.

#   - The 100x100 unit grid was too small, so I changed it to a 500x500 unit
#     grid.


import math
from random import randrange, random
from graphics import *


# CLASS
class the_GUI():
    def __init__(self, n_steps, distanceCL, first_distCL, last_distCL,
                 final_distCL, actual_distCL, straight_distCL):
        """Initializes the variables The "CL" on the end of some of the
        variables means that it is a class variable (differentiates the
        variable from the variables outside the class)."""
        
        self.n_steps = n_steps
        self.distanceCL = distanceCL
        self.first_distCL = first_distCL
        self.last_distCL = last_distCL
        self.final_distCL = final_distCL
        self.actual_distCL = actual_distCL
        self.straight_distCL = straight_distCL

        
    def draw_graph(self, window):
        """Draws the x and y lines on the window."""
        # Variables for this method
        x_axis = 0
        y_axis = 0

        # Draws lines
        x_axis = Line(Point(-20,0), Point(20,0))
        y_axis = Line(Point(0,-20), Point(0,20))
        x_axis.draw(window)
        y_axis.draw(window)


    def draw_random_walk(self, window, n_steps, distanceCL, final_distCL):
        """Draws the random walk line.
        - Takes in 4 parameters: window, n_steps (the value of the user-input
          variable num_steps), distanceCL, and final_distCL.
        - Uses a pseudo number random generator to determine the direction
          of the line. The distance from each previous point to the new point is
          calculated using the equation math.sqrt(x**2 + y**2) and each value is
          appended to the final_distances list."""

        # Variables for this method
        x = 0
        y = 0
        x1 = 0
        y1 = 0
        angle = 0
        step = 0

        # Draws the random walk line
        for i in range(n_steps):
            angle = random() * 2 * math.pi
            
            x1 = x + math.cos(angle)
            y1 = y + math.sin(angle)

            # Draws the line
            step = Line(Point(x,y), Point(x1,y1))
            step.setOutline('red')
            step.draw(window)
            
            x = x1
            y = y1
            
            distance = math.sqrt(x**2 + y**2)
            final_distances.append(distance)


    def print_results(self, first_distCL, last_distCL, final_distCL,
                      straight_distCL, actual_distCL):
        """Prints the results of the draw_random_walk() function.
        - Takes in 5 parameters: first_distCL, last_distCL, final_distCL,
          straight_distCL, and actual_distCL.
        - The straight_distCL is the distance between the first random number
          distance (first_distCL) and the last random number distance
          (last_distCL).
        - The actual_distCL is the sum of the distance values in the
          final_distCL list."""
    
        first_distCL = final_distCL[0]
        last_distCL = final_distCL[-1]

        straight_distCL = first_distCL + last_distCL
        actual_distCL = sum(final_distCL)

        print("Straight Distance:", round(straight_distCL), "units")
        print("Actual Distance:", round(actual_distCL), "units")

    
# VARIABLES
win = GraphWin('Random Walk', 500, 500)
win.setCoords(-20, -20, 20, 20)

num_steps = 0
distance = 0
first_dist = 0
last_dist = 0
final_distances = []
actual_dist = 0
straight_dist = 0


def main():
    """Asks for user-input for the num_steps. Creates a the_GUI object called
    randWalk_GUI."""
    
    while True:
        try:
            num_steps = int(input("Enter in a positive integer: "))
            while num_steps <= 0:
                num_steps = int(input("Please enter in a positive integer: "))
            break
        except ValueError:
            print("That is invalid input. Please enter in a positive integer.")

    randWalk_GUI = the_GUI(num_steps, distance, first_dist, last_dist,
                           final_distances, actual_dist, straight_dist)

    randWalk_GUI.draw_graph(win)

    randWalk_GUI.draw_random_walk(win, num_steps, distance, final_distances)
    
    randWalk_GUI.print_results(first_dist, last_dist, final_distances,
                               straight_dist, actual_dist)


# PROGRAM
main()
