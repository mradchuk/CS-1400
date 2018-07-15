# bowling_KT.py
# Programming Project #7: Bowling Team
# Created by Kyra Taylor, CS-1400-X01, Due August *SOMETHING****

# Original Problem: Create a scoring program for the bowling league that
# records the scores for each team member.

# Major steps and points of solution:
#   - The main() function is comprised of 6 functions: input_loop(),
#     list1_function(), list2_function(), list3_function(), calc_average()
#     and display_summary().
#       - input_loop() asks for data (player names and scores) until an
#         empty line is entered.
#       - The list 1, 2, and 3 functions sort the players_dict and then
#         append the results to the coorisponding lists.
#       - calc_average() calculates the average of the scores.
#       - display_summary() displays the results of the game.
#    - Uses a dictionary (players_dict) to assign the player name with his/her
#      score.
#    - Opens a text file called game_results.txt to write the information of the
#      program to.

# What I learned:
#    - How to write information to a text file.
#    - How to sort data by different criteria.
#    - How to format data on the console and in a text file.


from math import floor

# VARIABLES
input_done = False  # Boolean: Checks if the user is finished entering in data.
players_dict = {}
list1 = []
list2 = []
list3 = []
highScore_player = ""
average_score = 0
game_file = open("game_results.txt", "w")


# FUNCTIONS
def input_loop():
    """Loops until an empty line is entered."""
    
    player_info = str(input("Enter in the player name and score: "))
    
    while player_info != "":
        key, value = player_info.split(" ")
        if value == "300":
            key = key + "*"
        players_dict[key] = int(value)
        player_info = input("Enter in the player name and score: ")
        
    return input_done == True


def list1_function():
    """Prints out the information in the order received."""
    
    # Prints "List 1" to the console.
    print("\nList 1:")

    # Writes "List 1" to the game_results.txt file.
    game_file.write("List 1:\n")
    
    for key, value in players_dict.items():
        
        # Prints information to the console.
        print('{} {}'.format(key, value))

        # Writes information to the game_results.txt file.
        game_file.write('{} {}\n'.format(key, value))

        # Appends the keys and values from the players_dict to list1.
        list1.append(key)
        list1.append(players_dict[key])


def list2_function():
    """Orders the players by scores."""
    
    print("\nList 2:")
    
    game_file.write("\nList 2:\n")
    
    for key in sorted(players_dict, key=players_dict.__getitem__, reverse=True):

        print("{} {}".format(key, players_dict[key]))

        game_file.write('{} {}\n'.format(key, players_dict[key]))

        list2.append(key)
        list2.append(players_dict[key])

        
def list3_function():
    """Orders the players in alphabetical order."""

    print("\nList 3:")
    
    game_file.write("\nList 3:\n")
    
    for key in sorted(players_dict.keys()):
        
        print('{} {}'.format(key, players_dict[key]))
        
        game_file.write('{} {}\n'.format(key, players_dict[key]))
        
        list3.append(key)
        list3.append(players_dict[key])


def calc_average():
    """Calculate the average of the scores."""
    
    global average_score
    
    for score in list3[1::2]:
        average_score = average_score + score
        
    average_score = floor(average_score/(len(list3)/2))
    
    return average_score


def display_summary():
    """Displays the summary of the game."""

    print("\nSummary:")
    
    game_file.write("\nSummary:")
        
    highScore_player = list2[0]
    
    if highScore_player[-1] == "*":
        highScore_player = highScore_player.replace("*","")

    # Prints information to the console.
    print("Congratulations to %s, with the high score of %s!" %
          (highScore_player, list2[1]))
    print("The low score was %s. Better luck next time, %s." %
          (list2[-1], list2[-2]))
    print("The team average score is %s." % (average_score))

    # Writes information to the game_results.txt file.
    game_file.write("\nCongratulations to %s, with the high score of %s!" %
          (highScore_player, list2[1]))
    game_file.write("\nThe low score was %s. Better luck next time, %s." %
          (list2[-1], list2[-2]))
    game_file.write("\nThe team average score is %s." % (average_score))

    
def main():
    input_loop()
    list1_function()
    list2_function()
    list3_function()
    calc_average()
    display_summary()
    game_file.close()

    
# PROGRAM
main()
