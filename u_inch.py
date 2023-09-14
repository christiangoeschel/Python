# Tested on Python Version 3.9
# Author: Christian Goeschel Ndjomouo
# Sep 11 2023
# Description: A basic inch to cm converter (vice versa)


unit_type = ""              # Defines the users unit of measurement that he wants to convert from
factors = ['2.54','0.39']   # inch to cm , cm to inch factors in respective order
numbers_list = []           # The user can input as many numbers as he wants which will then be inserted into a list
final_string = ""           # The final string that will output all the conversions
interrupt_key = "c"         # If this key is entered the program will stop
user_input = ""
counter = 0

# Converter function takes the numbers_list as parameter
def converter(number_list):
    for i in number_list:

        global final_string
        cm =  round(float(i) * unit_type, 2)
        final_string += str(i) + " inches are " + str(cm) + " cm\n"


# Function that inserts numbers into the numbers_list
def add_nums():

    count = 0     # Counter for the while loop down below

    while count != 3:
            
        user_input = input("Type in the number or numbers you want to convert. Once you are done enter C to continue: ")

        if user_input.lower() == interrupt_key:
            count = 3
        elif user_input.isnumeric and float(user_input) not in numbers_list and len(user_input) > 0:
            numbers_list.append(float(user_input))
            continue
        else:
            break


# While loop and if-statements to determine the origin unit of measurement
while counter != 3:
    
    unit_type = input("Which unit of measurement do you want to convert from ?\n\n1 ) Inches to Cm \n2 ) Cm to Inches\n\nEnter C to cancel\n\nType in the option number here: ")

    if unit_type.lower() == interrupt_key:
        counter = 3
        break
    elif unit_type == "1" or unit_type == "2":
        unit_type = float(factors[int(unit_type) - 1])
        add_nums()
        converter(numbers_list) 
        counter = 3
    else:
        counter += 1
        continue



    
# Print out the final conversions
print("\n" + final_string)