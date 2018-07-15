# proj6_KT.py

# A graphical user interface that displays information about FluffShuffle
# Electronics employees.

# Created by Kyra Taylor, CS-1400-X01, Due July *SOMETHING*

# Original Problem: Create a payroll program that will read an employee data
# file and calculate each employee's net pay, and create an interactive
# graphical user interface.


# Person Who Helped Me:
#   - Morgan Taylor helped me figure out how to use the Next and Prev button
#     to change the information displayed on the GUI. I was trying to make
#     a frame for each employee, and then raise or lower the frame, depending
#     on whether the Next button was clicked or the Prev button was clicked.
#     Morgan suggested that I change only the text, which is what I did.


# Major Steps and Points of Solution:

#   - Uses a class, the_GUI, to hold methods and variables for the user
#     interface. the_GUI consists of 5 methods:

#        - __init__(): Creates the Next and Prev buttons for the GUI and
#          calls other methods to display text on the GUI.

#        - next_page(): Switches the employee displayed on the GUI to the next
#          employee by calling the makeform() method.

#        - prev_page(): Switches the employee displayed on the GUI to the
#          previous employee by calling the makeform() method.

#        - makeform(): Makes the text labels to be displayed on the GUI.

#        - remove_emplNum(): Removes the employee number item in each
#          employee list object, as it is not important for the GUI.


#   - Stores each employee as an employee list object. There are three
#     functions that contribute to making an employee list object:

#        - open_textFile(): Opens the text file and processes the lines by
#          calling the make_lines() function to make an employee list object.
#          Makes an instance of the_GUI called user_interface.

#        - make_lists(): Processes the lines of data from the text file and
#          makes them into employee list objects.

#        - calc_netPay(): Calculates the net pay based on an employee's hourly
#          wage and hours worked.

#   - The main() function sets up the tkinter and the window and makes the
#     File and Exit buttons.


# What I learned:
#   - My first step was breaking the large problem into smaller, yet still
#     general problems. These were the smaller problems: (1) make an employee
#     object, (2) make a function to open the text file, (3) make a function
#     to process the information in the text file, and (4) make a GUI.

#   - A major learning experience for me was learning how to utilize classes.
#     When I was first learning classes, they did not make sense to me,
#     especially the "self" keyword. Doing this project helped me better
#     understand why to use classes, how to set up the variables of the class,
#     and how to use the methods to manipulate the class information.


import tkinter as tk
from tkinter import filedialog

# CLASS
class the_GUI:
    
    def __init__(self, base, empls_list):
        """Initializes the variables and creates the GUI."""
        
        # Initializes variables
        self.index = 0
        self.empls_list = []

        # Creates the buttons previous and next buttons
        self.next_btn = tk.Button(base, text='Next', command=lambda:
                                  self.next_page(base))
        self.next_btn.place(x=230, y=160)

        
        self.prev_btn = tk.Button(base, text='Prev', command=lambda:
                                  self.prev_page(base))
        self.prev_btn.place(x=175, y=160)


        # Readys the text to display on the GUI
        self.remove_emplNum(empls_list)
        self.makeform(base, self.empls_list[self.index])

        
    def next_page(self, base):
        """Changes the employee information on the GUI to the next employee."""
        
        if self.index < len(self.empls_list)-1:
            self.index += 1
            empl_list = self.empls_list[self.index]
            self.makeform(base, empl_list)

            # Empties the empl_list for the next time the next_btn is clicked
            empl_list = []


    def prev_page(self, base):
        """Changes the employee information on the GUI to the previous
        employee."""
        
        if self.index > 0:
            self.index -= 1
            empl_list = self.empls_list[self.index]
            self.makeform(base, empl_list)

            # Empties the empl_list for the next time the prev_btn is clicked
            empl_list = []
    
        
    def makeform(self, base, empl_list):
        """Makes the text to display on the GUI."""
        
        # Variables for this method
        fields = ["Name:", "Address:", "Net Pay:"]
        rows = []
        y_val = 40

        # Displays textual information on the GUI
        for title, entry in zip(fields, empl_list):
            
            row = tk.Frame(base)

            title_label = tk.Label(row, width=10, text=title, anchor='w')
            empl_info = tk.Label(row, width=20, text=entry, anchor='w')
        
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            row.place(x=5, y=y_val)
        
            title_label.pack(side=tk.LEFT)
            empl_info.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            
            rows.append((title, empl_info))

            y_val += 30


    def remove_emplNum(self, empls_list):
        """Removes the employee number from each employee list."""

        # Variables for this method
        index_num = 0
        empl_list = []
        empl_list = empls_list[index_num]

        # Removes the employee number
        for employee in range(len(empls_list)):
            empl_list.pop(0)
            index_num += 1
            self.empls_list.append(empl_list)
            
            if index_num < len(empls_list):
                empl_list = empls_list[index_num]
            else:
                break
            


# FUNCTIONS

# Employee List Object Functions

def open_textFile(base):
    """Opens the text file, reads it, and then processes the lines to make
    an employee list object. Then uses those employee list objects to make
    an instance of the class, the_GUI, called user_interface.
    Takes in one parameters: base, which is the tkinter."""

    # Variables for this function
    empl_lists = []
    start_num = 0
    
    # Opens the input file for reading
    base.update()
    while True:
        try:
            filename = filedialog.askopenfilename()
            break
        except IOError:
            print("Could not read file. Please try again.")
            filename = filedialog.askopenfilename()
            
    input_file = open(filename, 'r')

    # Processes subsequent lines of the file
    data = input_file.readlines()
    
    # Processes lines of the file and makes them into employee list objects
    for lines in range(0, len(data)//4):
                       
        employee = make_lists(data, start_num)
    
        start_num += 4
        empl_lists.append(employee)

    # Closes the input_file
    input_file.close()
    
    # Makes an instance of the_GUI
    user_interface = the_GUI(base, empl_lists)

        
def make_lists(data, start_num):
    """Makes the employee list object.
    Takes in two parameters: data, which is where the information from the
    text file is stored, and start_num, which is the number that the for-loop
    starts iterating from."""

    # Variable for this method
    end_num = start_num + 4

    # Processes lines from the data and formats them for the empl_list list.
    empl_list = []

    for line in data[start_num:end_num]:
        line = line.strip('\n')
        empl_list.append(line)

    calc_netPay(empl_list)
    return empl_list


def calc_netPay(the_list):
    """Calculates an employee's net pay based on his/her hourly wage and
    hours worked.
    Takes in one parameter: the_list, which is the employee object list.
    Replaces the hourly wage and hours worked in the list with the net pay,
    and returns the list."""

    # Variables for this method
    net_pay = 0
    hourly_wage = 0
    hours_worked = 0

    line = the_list[3]
    hourly_wage, hours_worked = line.split(" ")

    hourly_wage = float(hourly_wage)
    hours_worked = float(hours_worked)

    # Calculates the net pay
    if hours_worked <= 40:
        net_pay = hourly_wage * hours_worked

    # Gives time-and-a-half for overtime (over 40 hours)
    else:
        net_pay = hourly_wage * 40
        hours_worked = hours_worked - 40
        net_pay = net_pay + (hourly_wage * hours_worked +
                            (hourly_wage * hours_worked * .5))

    # Deducts 20% for Federal income tax and 7.5% for state income tax
    net_pay = ((net_pay * .8) - (net_pay * .075))

    # Formats the net pay and appends it to the corresponding list
    net_pay = ("$%.2f" % (net_pay))
        
    the_list.pop(3)
    the_list.insert(3, net_pay)
    
    return the_list


# Main Function

def main():               
    """Sets up the tkinter window and makes the File and Exit buttons."""

    # Sets up the window
    root = tk.Tk()
    root.title("FluffShuffle Payroll")
    window = tk.Frame(master=root, width=300, height=200)
    window.pack()

    # Creates the buttons
    file_btn = tk.Button(root, text='File', command=lambda:
                         open_textFile(root))
    file_btn.place(x=5, y=2)
    
    exit_btn = tk.Button(root, text='Exit', command=root.destroy)
    exit_btn.place(x=55, y=2)
    

# PROGRAM
main()

