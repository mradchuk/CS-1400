# proj6.py

# Programming #6: A graphical user interface that displays
# information about FluffShuffle Electronics employees.
# CS-1400-X01, Due August 5, 2018.

# Original Problem: Create a payroll program that will read an employee data
# file and calculate each employee's net pay, and create an interactive
# graphical user interface.


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

#   - Uses a class, Employees, which holds each employee as an employee list
#     object. There are seven methods in the Employees class:

#        _ __init__(): Creates the File button and initializes the Employees
#          class variables.

#        - controller(): Controls the methods for the Employees class.

#        - open_textFile(): Opens the text file and checks for errors.

#        - process_file(): Reads the text file and calls make_employee to make
#          employee objects.

#        - make_lists(): Processes the lines of data from the text file and
#          makes them into employee list objects.

#        - calc_netPay(): Calculates the net pay based on an employee's hourly
#          wage and hours worked.

#        - makeInstance_GUI(): Makes an instance of the class, the_GUI, called
#          User_Interface.

#   - The main() function sets up the tkinter and the window, makes the Exit
#     button, and creates an instance of the Employees class called
#     Employee_Holder.


# What I learned:
#   - My first step was breaking the large problem into smaller, yet still
#     general problems. These were the smaller problems: (1) make an employee
#     object, (2) make a function to open the text file, (3) make a function
#     to process the information in the text file, and (4) make a GUI.

#   - A major learning experience for me was learning how to utilize classes.
#     When I was first learning Python classes, they did not make sense to me,
#     especially the "self" keyword. Doing this project helped me better
#     understand why to use classes, how to set up the variables of the class,
#     and how to use the methods to manipulate the class information.


import tkinter as tk
from tkinter import filedialog
import sys

# CLASSES

class the_GUI:
    """A class in which holds the information about the graphical user
    interface."""
    
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
            


class Employees:
    
    """A class in which holds the employee list objects. Each employee list
    object represents one employee and their information."""
    
    def __init__(self, base):
        """Initializes the variables for the Employees class and creates the
        File button. Takes in one parameter, base, which is the root. """
    
        # Initializes variables
        self.base = base
        self.empl_lists = []
        self.start_num = 0
        self.filename = ""
        self.data = []

        # Creates the File button
        self.file_btn = tk.Button(base, text='File', command=lambda:
                         self.controller("open_textFile"))
        self.file_btn.place(x=5, y=2)


    def controller(self, item):
        """Controls the methods for the Employees class. Takes in one parameter,
        item, which tells the controller which method to call."""
        
        if item == "error":
            print("Could not read file.")
            # Stops the other Employees class methods from running.
            sys.exit()

        elif item == "open_textFile":
            self.open_textFile()
            
        elif item == "process_file":
            self.process_file()

        elif item == "makeInstance_GUI":
            self.makeInstance_GUI()

        
    def open_textFile(self):
        """Opens the text file with a tkinter filedialog and checks for
        errors. If there are no errors, it tells the controller() method to call
        the process_file() method. If there is an error, it tells the
        controller() method to print out an error message to the console."""
        
        self.base.update()
        
        while True:
            
            try:
                self.filename = filedialog.askopenfilename()

                # If the file is not a text file:
                if not self.filename.endswith('.txt'):
                    self.controller("error")
                    break
                
                # If the file is a text file:
                self.controller("process_file")
                break
            
            except (IOError, ValueError):
                self.controller("error")
                break


    def process_file(self):
        """Reads the lines of the text file, and then processes the lines to
        make employee list objects. If there are no errors, it tells the
        controller() method to call the makeInstance_GUI() method."""
        
        # Variables for this method
        input_file = ""
        employe = []
        
        try:
            input_file = open(self.filename, 'r')

            # Processes subsequent lines of the file
            self.data = input_file.readlines()

            # Closes the input file
            input_file.close()
            
            # Makes the employee list objects
            for lines in range(0, len(self.data)//4):

                employee = self.make_lists()
        
                self.start_num += 4
                self.empl_lists.append(employee)

            # Calls the controller() method.
            self.controller("makeInstance_GUI")
                
        except (ValueError, IndexError, AttributeError):
            self.controller("error")

        
    def make_lists(self):
        """Makes the employee list object.
        Takes in one parameters, data, which is where the information from the
        text file is stored. Calls the calc_netPay() method, and then returns
        the employee list object."""

        # Variables for this method
        end_num = self.start_num + 4
        empl_list = []

        # Processes lines from the data and formats them for the empl_list list.
        try:
            for line in self.data[self.start_num:end_num]:
                line = line.strip('\n')
                empl_list.append(line)

            self.calc_netPay(empl_list)

            return empl_list
        
        except (ValueError, IndexError, AttributeError):
            self.controller("error")


    def calc_netPay(self, the_list):
        """Calculates an employee's net pay based on his/her hourly wage and
        hours worked.
        Takes in one parameter: the_list, which is the employee object list.
        Replaces the hourly wage and hours worked in the list with the net pay,
        and returns the list."""

        # Variables for this method
        net_pay = 0
        hourly_wage = 0
        hours_worked = 0

        try:
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

        except (ValueError, IndexError, AttributeError):
            self.controller("error")
            

    def makeInstance_GUI(self):
        "Makes an instance of the_GUI class called User_Interface."
        
        User_Interface = the_GUI(self.base, self.empl_lists)



# MAIN FUNCTION

def main():               
    """Sets up the tkinter window, makes the Exit button, and creates an
    instance of the Employees class called Employee_Holder."""
    
    # Sets up the window
    root = tk.Tk()
    root.title("FluffShuffle Payroll")
    window = tk.Frame(master=root, width=300, height=200)
    window.pack()

    # Creates the Exit button
    exit_btn = tk.Button(root, text='Exit', command=root.destroy)
    exit_btn.place(x=55, y=2)

    # Creates the Employees Class
    Employee_Holder = Employees(root)

    

# PROGRAM
main()

