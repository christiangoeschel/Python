# Tested on Python Version 3.9
# Author: Christian Goeschel Ndjomouo
# Sep 11 2023
# Description: This Python script handles the ID assignment for usernames in a preset list
#
# Module imports

import random   # Allows to randomly generate numbers

# Synchronize random module
random.seed()


# Variables, Sequences & Functions

usernames_list = ['Lamar','James','Jean','Jesse','Ronald','Marcus','Dwayne']    # Username list
user_dictionary = {}    # Contains usernames and their randomly assigned IDs

# ID generator function, takes 'a' as parameter which will be a usernames_list[] element
# which will be provided by the parse_to_dict() function.

def gen_id(a):
    
    username_len = len(a) 
    id_gen_factor = username_len // 3
    hex_id_portion = str(hex(username_len)) + str(id_gen_factor)

    for i in range(id_gen_factor):
        random_id_int = str(random.randint(100001,999999))

    global id
    id = random_id_int[0:len(random_id_int) // 2] + hex_id_portion + random_id_int[(len(random_id_int) // 2) + 1:]
    return id


# The parse_to_dict() function will iterate through the usernames_list[] and check whether the current username 
# is already on it and subsequently add or hop to the next list element to repeat the same check.

def parse_to_dict():

    for username in usernames_list:
        if username not in user_dictionary:
            user_dictionary[gen_id(username)] = username
        else:
            continue
    
    print(user_dictionary)


# The add_user() function will do a quick data type and length check on user input 
# and then add it as an ele in usernames_list[]

def add_user():

    user_input = input("Please type in your username\n(only alphabethic symbols and min. 8 characters long): ")
    counter = 0     # Counter for the while loop down below

    while counter != 3:
        if user_input.isalpha and user_input not in usernames_list and len(user_input) >= 8:
            usernames_list.append(user_input)
            print(usernames_list)
            counter = 3
        elif user_input in usernames_list:
            user_input = input("This username already exists. Please try a different one: ")
            counter += 1
        elif len(user_input) < 8:
            print("Username is",len(user_input),"characters long. Required are 8.\n")
            user_input = input("Type in a username again: ")
            counter += 1
        else:
            user_input = input("Please use alphabetic symbols only: ")
            counter += 1
            
    
# Invoke functions here:
add_user()
parse_to_dict()




