# rabbits.py
# Programming Project #4: Rabbits, Rabbits, Rabbits
# Created by Kyra Taylor, CS-1400-X01, due on June
# Person who helped me: Morgan Taylor

# Original Problem: Print a table and calculate how many months it will take
# until the number of rabbits exceeds the number of available cages.

# Major steps and points of solution:
#   - Prints a table with the values.
#   - Uses a while:True-loop to test if there are still cages available.

# What I learned:
#   - Morgan Taylor pointed out the pattern of the table to me, which is how
#     the number of babies equals the number of adults in the previous line,
#     and how the number of adults is equal to the number of previous
#     adults + the number of previous babies.
#   - I learned how to incorporate Booleans and use them in while-loops.


# FUNCTION

def main():

    # VARIABLES
    max_num_cages = 500
    have_cages = True # Boolean for if there are still cages available or not.
    month_num = 1
    num_adults = 1
    beg_num_adults = 0 # The number of adult pairs before the babies are
                       # added to the adults.
    num_babies = 0
    total_cages = num_adults + num_babies

    # FUNCTION
    print("Table of rabbit pairs\n")

    print("Month\tAdults\tBabies\tTotal")

    print(str(month_num) + '\t' + str(num_adults) + '\t' + str(num_babies)
          + '\t' + str(total_cages))

    while have_cages == True:
        month_num += 1 # Adds 1 to the month number.
        beg_num_adults = num_adults # The number of adults before the babies
                                    # become adults.
    
        num_adults += num_babies

        num_babies = beg_num_adults # The number of new babies is the number of
                                # adults (before the number of babies was added).

        total_cages = num_adults + num_babies

        print(str(month_num) + '\t' + str(num_adults) + '\t' + str(num_babies)
              + '\t' + str(total_cages))
       
        if total_cages > 500:
            have_cages = False
        
        else:
            have_cages = True

        if have_cages == False:
            print("\nCages will run out in month %s." % (month_num))


# PROGRAM
main()
