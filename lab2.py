#*****************************************************************************
# Author:       Grayson Hanna and Josh Meyer
# Assignment:   CIS-133Y Lab2
# Date:         10/3/2026
# Description:  Collect product information to determine total purchase prices
# Input:        str product_name, float price, int count, str/int selected
# Output:       str product_name, float price, int count, float total
# Sources:      
#*****************************************************************************
#
#
from datetime import datetime

# Program polish and testing Grayson Hanna

# Collects Product Name, the Price of the product, and the amount sold to
# calculate the total purchase price.
# - Josh Meyer
def collectData():
    user_input = input("Add a new purchase? (y/N): ")
    # Loops through as long as "y" is provided
    while user_input.lower() == "y":
        # Asks for the Product Name
        product_name = input("Product Name: ")
        price = 0.0
        # Loops through to validate the Price input is an int or float
        while price == 0.0:
            price = input("Price: $")
            try:
                # Try to cast a float
                float(price)
            except:
                # Failed to conver to float, reset and tell the user to try
                # again
                price = 0.0
                print("Invalid input")
        count = 0
        # Loops through to validate the Count input in an int
        while count == 0:
            count = input("Number Sold: ")
            if not str.isdigit(count):
                # Failed to validate as int, reset and tell the user to try
                # again
                count = 0
                print("Invalid input")
        # Convert the Price to float and multiply by the converted int value
        # of count, then round to 2 decimals
        total = round(float(price) * int(count), 2)
        # Display the output to the user with the total price
        # Example - *  Banana - $0.75 x2: $1.50 
        print("*  {product} - ${price:.2f} x{count}: ${total:.2f}".format(product = 
            product_name, price = float(price), count = int(count), total = float(total)))
        # Ask if additional items to add
        user_input = input("Add a new purchase? (y/N): ")

# The main program loop presents the name of the application and the current
# time that it was executed. It provides a menu for selecting which 
# computation the user wishes to execute or quit the application.
# - Josh Meyer
def main():
    selected=""
    while selected.lower() != "q":
        # The name of the Application to display
        app_name = "Profit calculator"
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
        print("*{spacing}{naming}{spacing}*".format(spacing = (" " * whitespace),
            naming = app_name))
        # Print "*" on either side of the datetime stamp while centering it
        #  with whitespace.
        whitespace = int((border_length - len(current_time_string))/2)
        print("*{spacing}{naming}{spacing}*".format(spacing = (" " * whitespace),
            naming = current_time_string))
        # Print bottom border
        print("*" * (border_length +2))
        # Print menu options and receive input
        print("1) Enter product info")
        print("q) Quit Application")
        selected=input("> ")
        # If tree for parsing the user input
        if str.isdigit(selected):
            if int(selected) == 1:
                collectData()
        print("")
#Josh Meyer
main()