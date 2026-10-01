#*****************************************************************************
# Author:       Grayson Hanna and Josh Meyer
# Assignment:   CIS-133Y Lab2
# Date:         10/1/2026
# Description:  
# Input:        
# Output:       
# Sources:      
#*****************************************************************************
#
#
# Lab Requirements:
# \ Accept at least a numeric and a string value
# - Perform at least one calculation with arithmetic operators and at least
#   one compound operator
# X Use at least one date-time function
# X Use round()
# - Use format()
# X Include at least one chaining function
# X At least one output that has concatenated string ("..." + "...")
from datetime import date,datetime,time

def collectData():
    pass


# The main program loop presents the name of the application and the current
# time that it was executed. It provides a menu for selecting which 
# computation the user wishes to execute or quit the application.
# - Josh Meyer
def main():
    selected=""
    while selected.lower() != "q":
        # The name of the Application to display
        app_name = "Application Name"
        # Get the current date and time
        current_time = datetime.now()
        # Format current_time to this style: 2026-10-01 12:10:05 PM
        current_time_string = str(current_time.date()) + \
            " " + str(current_time.strftime("%H:%M:%S %p"))
        # Determine which is longer, datetime stamp or the application name
        #  and add some padding
        border_length = len(current_time_string)
        if len(app_name) > border_length:
            border_length = len(app_name)
        border_length+=2
        # Print top border
        print("*" * (border_length +2))
        # Print "*" on either side of the Application Name while centering it
        #  with whitespace.
        whitespace = int((border_length - len(app_name))/2)
        print("*" + (" " * whitespace) +
            app_name + (" " * whitespace) + "*")
        # Print "*" on either side of the datetime stamp while centering it
        #  with whitespace.
        whitespace = int((border_length - len(current_time_string))/2)
        print("*" + (" " * whitespace) +
            current_time_string + (" " * whitespace) + "*")
        # Print bottom border
        print("*" * (border_length +2))
        # Print menu options and receive input
        print("1) Enter Info")
        print("q) Quit Application")
        selected=input("> ")
        # If tree for parsing the user input
        if selected == "1":
            collectData()
        print("")

main()