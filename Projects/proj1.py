# proj1.py

# Programming Project #1: Simple Tip Calculator. A simple program that uses a
# function called calculate_tip(meal_cost) to calculate a tip based on the
# quality of the service.
# CS 1400-X01, due on June 1, 2018


# Original Problem: Based on the quality of service, calculate the tip and total
# cost of the meal.

# Important Points:
# - Uses a function called calculate_tip to calculate the cost of an excellent
#   service tip, an average service tip, and a poor service tip.
# - Uses the function calculate_tip to print out the results.


# FUNCTION

# calculate_tip Function: First calculates the amount of the tip based on the
# quality of service (excellent, average, and poor), and then calculates the
# total cost of the meal.
# Takes in one parameter, meal_cost, which is the user-input value of how much
# the meal costs before the tip is accounted for.
def calculate_tip(meal_cost):

  # Variables of the calculate_tip function
  excellent_tip = meal_cost * .20 # The excellent tip is 20% of the meal cost.
  average_tip = meal_cost * .15 # The average tip is 15% of the meal cost.
  poor_tip = meal_cost * .10 # The poor tip is 10% of the meal cost.
  
  # Prints the result of the calculate_tip function
  print("""\nCost of meal: $%.2f
Excellent Service tip: $%.2f total: $%.2f
Average Service tip: $%.2f total: $%.2f
Poor Service tip: $%.2f total: $%.2f""" %
        (meal_cost, excellent_tip, (excellent_tip + meal_cost),
         average_tip, (average_tip + meal_cost), poor_tip,
         (poor_tip + meal_cost)))


# PROGRAM
cost_of_meal = float(input("Enter the cost of the meal: $"))
calculate_tip(cost_of_meal)


# Challenges and Learning
# Challenge: The most challenging part of this project for me was
# figuring out how to format floats with two decimal points.

# Learning: What I learned from this project is how to format
# floats with two decimal points. In the past, when I have searched
# how to do this, I saw the symbol "%.2f" but did not understand what
# its purpose was. By doing this project, I realized that it is similar
# to the "%s" symbol, which inserts a string variable. The "%.2f"
# symbol inserts a float number, rounded to 2 decimal points.
