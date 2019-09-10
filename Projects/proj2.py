# proj2.py

# Programming Project #2: Geometric Shapes: A program that draws the classic 5
# platonic platonic solides using lines, shapes, and colors.
# CS 1400-X01

# Original Problem: Draw the classic 5 platonic platonic solides using lines, shapes,
# and colors.


import turtle
import math

screen = turtle.Screen() # Names the turtle screen to screen.
screen.colormode(255) # Changes the color mode to rgb(255).
pen = turtle.Turtle() # Names the turtle to pen
pen.speed(0) # Increases the speed of the pen.


# BASIC FUNCTIONS

# draw_triangle Function: Draws a triangle. Takes in 9 arguments: r, g, b are the values
# for the rgb color, x and y are the coordinates of the first point, x1 and y1 are the
# coordinates of the second point, and x2 and y2 are the coordinates of the third point.
def draw_triangle(r, g, b, x, y, x1, y1, x2, y2):
  pen.penup() # Lifts the pen up to prevent it from drawing.
  pen.color(r,g,b)
  pen.goto(x, y)
  pen.begin_fill() # Begins filling the shape with the rgb color specified.
  pen.pendown() # Sets the pen down, readying it to draw.
  pen.goto(x1, y1)
  pen.goto(x2, y2)
  pen.end_fill() # Stops filling the shape with the rgb color specified.
  pen.penup() # Lifts the pen up again.

# draw_square Function: Draws a square. Takes in 11 arguments: r, g, b are the values
# for the rgb color, x and y are the coordinates of the first point, x1 and y1 are the
# coordinates of the second point, x2 and y2 are the coordinates of the third point,
# and x3 and y3 are the coordinates of the fourth point.
def draw_square(r, g, b, x, y, x1, y1, x2, y2, x3, y3):
  pen.penup()
  pen.color(r,g,b)
  pen.goto(x, y)
  pen.begin_fill()
  pen.pendown()
  pen.goto(x1, y1)
  pen.goto(x2, y2)
  pen.goto(x3, y3)
  pen.end_fill()
  pen.penup()
  
# draw_pentagon Function: Draws a pentagon. Takes in 13 arguments: r, g, b are the values
# for the rgb color, x and y are the coordinates of the first point, x1 and y1 are the
# coordinates of the second point, x2 and y2 are the coordinates of the third point, x3 and
# y3 are the coordinates of the fourth point, and x4 and y4 are the coordinates of the fifth
# point.
def draw_pentagon(r, g, b, x, y, x1, y1, x2, y2, x3, y3, x4, y4):
  pen.penup()
  pen.color(r,g,b)
  pen.goto(x, y)
  pen.begin_fill()
  pen.pendown()
  pen.goto(x1, y1)
  pen.goto(x2, y2)
  pen.goto(x3, y3)
  pen.goto(x4, y4)
  pen.end_fill()
  pen.penup()

  
# FUNCTIONS FOR THE 5 PLATONIC SOLIDS

# draw_tetrahedron Function: Draws a tetrahedron, a polyhedron with four faces.
def draw_tetrahedron():
  draw_triangle(255, 252, 183, 0, 500, 50, 420, 0, 440)
  draw_triangle(255, 255, 0, 0, 500, -50, 420, 0, 440)
  draw_triangle(255, 215, 0, 0, 440, -50, 420, 50, 420)
  
# draw_cube Function: Draws a cube, a polyhedron with six faces.
def draw_cube():
  draw_square(0, 0, 0, 0, 300, -40, 310, -40, 360, 0, 350)
  draw_square(190, 190, 190, 0, 300, 40, 310, 40, 360, 0, 350)
  draw_square(105, 105, 105, 0, 350, -40, 360, 0, 370, 40, 360)

# draw_octahedron Function: Draws an octahedron, a polyhedron with eight faces.
def draw_octahedron():
  draw_triangle(249, 199, 239, 0, 260, -10, 180, -50, 200)
  draw_triangle(255, 211, 245, 0, 260, -10, 180, 50, 200)
  draw_triangle(239, 158, 201, 50, 200, 5, 150, -10, 180)
  draw_triangle(232, 113, 176, -10, 180, -50, 200, 5, 150)

# draw_icosahedron Function: Draws an icosahedron, a polyhedron with 20 faces.
def draw_icosahedron():
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
  
# draw_dodecahedron Function: Draws a dodecahedron, a polyhedron with twelve faces.
def draw_dodecahedron():
  draw_pentagon(64, 224, 208, -20, -135, -50, -100, -25, -60, 15, -68, 18, -115)
  draw_pentagon(111, 247, 226, 18, -115, 40, -120, 55, -85, 38, -52, 15, -68)
  draw_pentagon(142, 255, 226, 15, -68, 38, -52, 15, -35, -22, -40, -25, -60)
  draw_pentagon(63, 193, 187, -25, -60, -22, -40, -45, -65, -58, -101, -50, -100)
  draw_pentagon(12, 108, 117, -50, -100, -20, -135, -15, -150, -45, -130, -58, -101)
  draw_pentagon(0, 139, 139, -15, -150, -20, -135, 18, -115, 40, -120, 20, -145)
  
  
# PROGRAM
draw_tetrahedron()
draw_cube()
draw_octahedron()
draw_icosahedron()
draw_dodecahedron()
pen.hideturtle()
