# File: chaos_ch1_pe7.py

# A simple program illustrating chaotic behavior.

# Chapter 1, Programming Exercises #7: (Advanced) Modify the Chaos program so
# that it accepts two inputs and then prints a table with two columns similar
# to the one shown in Section 1.8. (Note: You will probably not be able to get
# the columns to line up as nicely as those in the example. Chapter 5 discusses
# how to print numbers with a ﬁxed number of decimal places.)

print("This program illustrates a chaotic function")

num1 = eval(input("Enter a number between 0 and 1: "))
num2 = eval(input("Enter a number between 0 and 1: "))

print("\ninput\t ", num1, "\t\t ", num2)
print("--------------------------------")

for i in range(10):
    num1 = 3.9 * num1 * (1 - num1)
    num2 = 3.9 * num2 * (1 - num2)

    print("\t%.6f\t%.6f" % (num1, num2))

