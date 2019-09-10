# farmer_john.py
# Programming Project #3: Farmer John's Field
# CS-1400-X01

# Original Problem: Given the length of the side of the square, calculate
# the area of the shaded area of the map.

# Main points of my solution:
#   - Uses user-defined functions with pre-defined functions (such as
#     turtle.circle, turtle.setpos, etc.) to draw the map.
#   - Uses the user-defined function calculate_shaded_area() to calculate
#     the area of the shaded area.
#   - Uses a while True: loop to test for valid input.

# What I learned:
#   - I learned how to use a while True: loop with try: and except <Error>:
#   - I learned how to use for-loops and the zip() function to draw shapes.
#   - I learned how to use simple math and logical thinking to make a function
#     to calculate area.


import turtle
import math

screen = turtle.Screen()
screen.title("Farmer John")
screen.setup(500,500)
screen.colormode(255)
pen = turtle.Turtle()
pen.speed(0)


# FUNCTIONS

def draw_square():
    """Draws a square. Uses a for-loop to draw the four sides of the square,
    and fills the square with the color gray."""
    pen.penup()
    pen.setpos(-100, 130)
    pen.color(118, 120, 124)
    pen.begin_fill()
    pen.pendown()
    for i in range(4):
        pen.forward(200)
        pen.right(90)
    pen.end_fill()

def draw_circles():
    """Draws four circles with a radius of 100. Uses a for-loop and the
    zip() function to iterate between two lists: x_coordinates and
    y_coordinates. The combination of the two are the center points for the
    circles. The fill color is white and the outline color is black."""
    x_coordinates = [-100, -100, 100, 100]
    y_coordinates = [-170, 30, -170, 30]
    pen.pencolor(0, 0, 0)
    pen.color("black", "white") # Sets the outline color to black
                                # and the fill color to white.
    for x_coord, y_coord in zip(x_coordinates, y_coordinates):
        pen.begin_fill()
        pen.penup()
        pen.setpos(x_coord, y_coord)
        pen.pendown()
        pen.circle(100)
        pen.end_fill()

def draw_square_outline():
    """Draws the outline of a square. Uses a for-loop to draw the four sides of
    the square. The outline color is black."""
    pen.penup()
    pen.setpos(-100, 130)
    pen.pencolor("black")
    pen.pendown()
    for i in range(4):
        pen.forward(200)
        pen.right(90)
    pen.end_fill()
    
def write_text():
    """Writes the letters "A", "B", "C", "D", each letter in one the of the
    circles. Uses a for-loop and the zip() function to iterate through 3 lists:
    letters, x_coordinates, and y_cooridnates."""
    letters = ["A", "B", "C", "D"]
    x_coordinates = [-140, 105, -140, 105]
    y_coordinates = [120, 120, -130, -130]
    pen.penup()
    pen.pendown()
    for letter, x_coord, y_coord in zip(letters, x_coordinates, y_coordinates):
        pen.penup()
        pen.setpos(x_coord, y_coord)
        pen.pendown()
        pen.write(letter, move=False, align="left",
                  font=("Arial", 60, "normal"))

def calculate_shaded_area():
    """Calculates the area of the shaded area on the map. Takes user-input for
    the length of the side (side_length).
       - In the square, there are four 1/4 circles, which equals a full circle.
         The area of the shaded area is the area of the square minus the area
         of a circle."""
    side_length = float(input("Enter in the square side length: "))
    radius = side_length/2
    circle_area = round(math.pi * radius**2, 2)
    shaded_area = side_length**2 - circle_area
    print("The area of the shaded area is %.2f units squared." % (shaded_area))

def main():
    draw_square()
    draw_circles()
    draw_square_outline()
    write_text()
    while True:
        try:
            calculate_shaded_area()
            break
        except ValueError:
            print("That is not a valid input. This program will now stop.")
            break # Exits the program.


# PROGRAM
main()
