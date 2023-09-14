# Tested on Python Version 3.9
# Author: Christian Goeschel Ndjomouo
# Sep 13 2023
# Description: This Python program asks the user to enter a monthly income before taxes, obviously,
#              and the program returns the monthly net income and the amount of paid taxes.


# User input verification fucntion

def input_check():
    
    global income
    # User input stored in variable 'income'
    income = input("Please enter your monthly income before taxes: ")

    global married
    married = input("Type in 'S' for single or 'M' for married: ")


    # Checking if the user input is a valid number
    if income.isnumeric() and married.isalpha():
        income = float(income)  # Storing the numeric value as a float
        married = married
    else: 
        income = 0.0    # Store 0.0 as value which will trigger an error the tax_calc() fucntion
        married = "None"



# Final message function

def final_message(taxrate):
        
        print("Your monthly net income is:", str( income - (income * taxrate) ) + "$" ,end="\n")
        print("You are paying",str(income * taxrate) + "$ per month.")
        print("Tax rate:", int(taxrate * 100),"%")


def tax_calc(mon_income,status):

    tax_rate = 0

    # if statements for tax bracket determination
    if mon_income > 4000.0 and status.upper() == "S":
        
        tax_rate = 0.26
        final_message(tax_rate)

    elif mon_income > 4000.0 and status.upper() == "M":
        
        tax_rate = 0.22
        final_message(tax_rate)
         

    elif mon_income <= 4000.0 or status.upper() == "S" or status.upper == "M" and mon_income != 0.0:
        
        tax_rate = 0.18
        final_message(tax_rate)

    else:
        print("Invalid input!")


input_check()
tax_calc(income,married)