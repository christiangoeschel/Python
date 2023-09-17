# Tested on Python Version 3.9
# Author: Christian Goeschel Ndjomouo
# Sep 13 2023
# Description: This Python program asks the user to enter a a date in DD / MM /YYYY format,
#              and the program checks whether the date is valid or not.


# Request input from user in DD / MM / YYYY format
def input_req():

    # User input prompt and split of the date components with "/" as delimiter
    user_input = input("Please type in a date in DD / MM / YYYY format: ").split('/')

    global split_date
    split_date = []

    # For loop with an nested try:except statement that tries to iterate through the date_list list and 
    # stores each <str> list value as an <int> value

    if len(user_input) == 3:

            try:
                split_date.append(int(user_input[0]))    # List value in <str> to <int> conversion
                split_date.append(int(user_input[1]))
                split_date.append(int(user_input[2]))

            except:
                print("\nFatal Error!\n\nExpected input type: numeric\nActual input type: alphabectic/symbolic\nPlease try again.")

    else:
        split_date = None
        print("Fatal Error! Wrong date format. Expected DD/MM/YYYY")

    return split_date
    
        

# Date validation function
# Here the date will be checked on its numeric legitimacy 
def date_checker(date):

    leap_year = False   # Leap year boolean variable

    # Checking whether year is a leap year or not
    # Divisible by 4 without a remainder => Leap year
    
    if date != None:

        if date[-1] % 4 == 0:
        
            leap_year = True

    # Condition tree if date[-1] is a leap year

    if date == None:
        print("\n\nDATE IS INVALID!\n\n")
        exit

    elif leap_year:

            if date[1] == 2 and date[0] > 29:

                print("Invalid!",date[-1],"is a leap year. Day cannot be", date[0])
                exit
            
            elif date[0] >= 32 or date[0] <= 0:

                print("Invalid! Day cannot be", date[0])
                exit

            elif date[1] >= 13 or date[1] <= 0:

                print("Invalid! Month cannot be", date[1])
                exit
            
            elif date[-1] <= 0:

                print("Invalid! Year cannot be", date[-1])
                exit
            
            else:
                pass

            
    # Condition tree if date[-1] is NOT A LEAP YEAR
    else:

            if date[1] == 2 and date[0] > 28:

                print("Invalid!",date[-1],"is not a leap year. So February only has 28 days. Day cannot be", date[0])
                exit
            
            elif date[0] >= 32 or date[0] <= 0:

                print("Invalid! Day cannot be", date[0])
                exit

            elif date[1] >= 13 or date[1] <= 0:

                print("Invalid! Month cannot be", date[1])
                exit
            
            elif date[-1] <= 0:

                print("Invalid! Year cannot be", date[-1])
                exit
            
            else:
                print("\n\nDATE IS VALID!\n\n")
                exit

        
# Invoke the date_checker function with the return of input_req() as argument
date_checker(input_req())



        
        



    

