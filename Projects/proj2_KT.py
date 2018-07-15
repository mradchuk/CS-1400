# proj2_KT.py

# Programming Project #2: Geometric Shapes: A program that draws the classic 5
# platonic platonic solids using lines, shapes, and colors.
# Created by Kyra Taylor, CS 1400-X01, due on June 3, 2018

# Original Problem: Draw the classic 5 platonic platonic solids using lines,
# shapes, and colors.

# Major steps and points of my solution include:
#   - Uses Python Turtles graphics to draw the shapes.
#   - Uses the predefined-functions from the Python Turtles library, including
#     turtle.penup(), turtle.color(), turtle.begin_fill(), turtle.goto(),
#     turtle.end_fill(), and turtle.pendown().
#   - This program uses user-defined functions to draw shapes.
#      - The three basic user-defined functions are the draw_triangle(),
#        draw_square(), and draw_pentagon() functions.
#      - The basic functions are the foundation for the functions that draw the 5
#        platonic solids: draw_tetrahedron(), draw_cube(), draw_octahedron(),
#        draw_icosahedron(), and draw_dodecahedron().

# What I learned
#   - My biggest challenge at the beginning was trying to figure out how to draw
#     a basic triangle. I used the predefined-functions, turtle.forward(),
#     turtle.right(), and turtle.left(), to draw a triangle. This was not an
#     efficient method, as it was mostly trial and error.
#   - In an attempt to make drawing a triangle more efficient, I tried using
#     trigonometry to calculate the length of a side of a triangle, and this
#     was the function I tried:
#     pen.forward(math.sqrt((x1 - x)**2 + (y1 - y)**2)).
#   - I also attempted using trigonometry to find the angle of a triangle point.
#   - Once I came across the pen.goto() function, I was able to complete the
#     program faster and more efficiently.
#   - I also learned about the Python Turtle Graphics. I did not know that the
#     Python IDLE was capable of using graphics.
#   - Another lesson I learned was how to use for-loops to iterate between
#     two lists.


import turtle

screen = turtle.Screen()
screen.setup(300, 1100)
screen.title("Platonic Platonic Shapes")
screen.colormode(255)
pen = turtle.Turtle()
pen.speed(0)


# BASIC FUNCTIONS

def draw_triangle(r, g, b, x, y, x1, y1, x2, y2):
  """Draws a triangle. Takes in 9 arguments: r, g, b are the values for the
  rgb color, x and y are the coordinates of the first point, and x1 and y1 are
  the coordinates of the second point, and x2 and y2 are the coordinates of the
  third point."""
  variables_x = [x, x1, x2]
  variables_y = [y, y1, y2]
  pen.penup()
  pen.color(r,g,b)
  pen.goto(x, y)
  pen.begin_fill()
  pen.pendown() 
  for x_coord, y_coord in zip(variables_x, variables_y):
    pen.goto(x_coord, y_coord)                           
  pen.end_fill()


def draw_square(r, g, b, x, y, x1, y1, x2, y2, x3, y3):
  """Draws a square. Takes in 11 arguments: r, g, b are the values for the rgb
  color, x and y are the coordinates of the first point, x1 and y1 are the
  coordinates of the second point, x2 and y2 are the coordinates of the
  third point, and x3 and y3 are the coordinates of the fourth point."""
  variables_x = [x, x1, x2, x3]
  variables_y = [y, y1, y2, y3]
  pen.penup()
  pen.goto(x, y)
  pen.color(r,g,b)
  pen.begin_fill()
  pen.pendown()
  for x_coord, y_coord in zip(variables_x, variables_y):
    pen.goto(x_coord, y_coord)
  pen.end_fill()

  
def draw_pentagon(r, g, b, x, y, x1, y1, x2, y2, x3, y3, x4, y4):
  """Draws a pentagon. Takes in 13 arguments: r, g, b are the values for the
  rgb color, x and y are the coordinates of the first point, x1 and y1 are the
  coordinates of the second point, x2 and y2 are the coordinates of the
  third point, x3 and y3 are the coordinates of the fourth point, and x4 and
  y4 are the coordinates of the fifth point."""
  variables_x = [x, x1, x2, x3, x4]
  variables_y = [y, y1, y2, y3, y4]
  pen.penup()
  pen.color(r,g,b)
  pen.goto(x, y)
  pen.begin_fill()
  pen.pendown()
  for x_coord, y_coord in zip(variables_x, variables_y):
    pen.goto(x_coord, y_coord)
  pen.end_fill()


# FUNCTIONS FOR THE 5 PLATONIC SOLIDS

def draw_tetrahedron():
  """Draws a tetrahedron, a polyhedron with four faces."""
  draw_triangle(255, 252, 183, 0, 500, 50, 420, 0, 440)
  draw_triangle(255, 255, 0, 0, 500, -50, 420, 0, 440)
  draw_triangle(255, 215, 0, 0, 440, -50, 420, 50, 420)

def draw_cube():
  """Draws a cube, a polyhedron with six faces."""
  draw_square(0, 0, 0, 0, 300, -40, 310, -40, 360, 0, 350)
  draw_square(190, 190, 190, 0, 300, 40, 310, 40, 360, 0, 350)
  draw_square(105, 105, 105, 0, 350, -40, 360, 0, 370, 40, 360)

def draw_octahedron():
  """Draws an octahedron, a polyhedron with eight faces."""
  draw_triangle(249, 199, 239, 0, 260, -10, 180, -50, 200)
  draw_triangle(255, 211, 245, 0, 260, -10, 180, 50, 200)
  draw_triangle(239, 158, 201, 50, 200, 5, 150, -10, 180)
  draw_triangle(232, 113, 176, -10, 180, -50, 200, 5, 150)

def draw_icosahedron():
  """Draws an icosahedron, a polyhedron with twenty faces."""
  draw_triangle(255, 73, 73, 30, 50, 0, 100, -30, 50)
  draw_triangle(180, 26, 26, 30, 50, 0, 10, -30, 50)
  draw_triangle(253, 91, 91, 30, 50, 45, 90, 0, 100)
  draw_triangle(217, 39, 39, -30, 50, -45, 90, 0, 100)
  draw_triangle(219, 43, 43, -30, 50, -45, 40, -45, 90)
  draw_triangle(239, 127, 127, 30, 50, 45, 40, 45, 90)
  draw_triangle(193, 31, 31, 30, 50, 45, 40, 0, 10)
  draw_triangle(153, 30, 30, -30, 50, -45, 40, 0, 10)
  draw_triangle(249, 139, 139, 0, 100, 0, 115, 45, 90)
  draw_triangle(247, 106, 106, 0, 100, 0, 115, -45, 90)
  
def draw_dodecahedron():
  """Draws a dodecahedron, a polyhedron with twelve faces."""
  draw_pentagon(64, 224, 208, -20, -135, -50, -100, -25, -60, 15, -68, 18, -115)
  draw_pentagon(111, 247, 226, 18, -115, 40, -120, 55, -85, 38, -52, 15, -68)
  draw_pentagon(142, 255, 226, 15, -68, 38, -52, 15, -35, -22, -40, -25, -60)
  draw_pentagon(63, 193, 187, -25, -60, -22, -40, -45, -65, -58, -101, -50, -100)
  draw_pentagon(12, 108, 117, -50, -100, -20, -135, -15, -150, -45, -130, -58, -101)
  draw_pentagon(0, 139, 139, -15, -150, -20, -135, 18, -115, 40, -120, 20, -145)

  
# MAIN FUNCTION
def main():
  """Draws the 5 platonic platonic shapes."""
  draw_tetrahedron()
  draw_cube()
  draw_octahedron()
  draw_icosahedron()
  draw_dodecahedron()
  pen.hideturtle()


# PROGRAM
main()
