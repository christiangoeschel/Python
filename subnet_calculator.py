# Tested on Python Version 3.9
# Author: Christian Goeschel Ndjomouo
# Sep 17 2023
# Description: This program takes a random IPv4 address, Subnet Mask and/or CIDR as input
#              Returns detailed information about the Network like the Network ID, Network range, First and Last 
#              useable host addresses,total amount of hosts, total amount of useable hosts, broadcast address,
#              Subnet Mask and CIDR notation. More features may be added in the future.

# Import modules
import sys
import re

# Variables

ip_list = []
submask_list = []


# Function to retrieve IP and Subnet Mask
def input_req():

    global ip_input
    global sm_input

    ip_input = input("""Please type in an IPv4 address\n
                     [ Allowed format ]
                     Standard: XXX.XXX.XXX.XXX\n
                     Type in here: """)
    
    
    sm_input = input("""\nNow, please type in the Subnet Mask.\n
                     [ Allowed formats ]
                     Standard: XXX.XXX.XXX.XXX
                     CIDR: /XX  ( Example: /23 )\n
                     Type in here: """)
    
    return ip_input, sm_input



    
    

# Function for the splitting of the octects or CIDR notation numeric values from ' . ' or ' / '

def splitter(valid_input):

    valid_ip = valid_input[0]
    valid_sm = valid_input[1]

    valid_ip = valid_ip.split('.')  # Splits the numeric values from the ' . ' out of each octet
    
    # If the length is greater than 3 it cannot be CIDR but the traditional Subnet mask
    if len(valid_sm) > 3:
        valid_sm = valid_sm.split('.')  # Splits the numeric values from the ' . ' out of each octet
    
    else:
        valid_sm = valid_sm.split('/')  # Splits the numeric value from the ' / ' 
        del valid_sm[0]

    return valid_ip, valid_sm



# This function converts the subnet mask into binary and calculates the CIDR 
# by counting how many occurences of "1" there are 
def sm_bin_converter(sm_bin):

    sm_counter = 0

    for i in range(0,32):

        if "1" in sm_bin[i]:

            sm_counter += 1

        else:
            continue
    
    return sm_counter




# This function calculates the first and lost host of the network range
def calc_hosts_bin(bin_net_id, bin_brdcst, cidr_notation):

    global cidr
    cidr = cidr_notation

    if cidr != 32:
        # Flipping last binary value into a one
        first_host_bin = bin_net_id[0:-1] + "1"
        last_host_bin = bin_brdcst[0:-1] + "0" 

    else:
        first_host_bin = bin_net_id
        last_host_bin = bin_brdcst

    return first_host_bin, last_host_bin




# This function converts the first and last host binary values into decimal
def calc_hosts(first_host_bin,last_host_bin):

    global first_host
    global last_host
    global first_host_octet
    global last_host_octet

    first_host_octet = ""
    last_host_octet = ""
    first_host = ""
    last_host = ""

    for i in range(0,4):
        for binary in range(0,8):

            first_host_octet += first_host_bin[binary]
            last_host_octet += last_host_bin[binary]
        
        if i != 3:

            # Appending the converted decimal octet
            first_host += str(int(first_host_octet, 2)) + "."
            last_host += str(int(last_host_octet, 2)) + "."
            
            # Stripping the leading octets
            first_host_bin = first_host_bin[8:]
            last_host_bin = last_host_bin[8:]

            # Clearing the temporary octet store for the next conversion
            first_host_octet = ""
            last_host_octet = ""
            
            continue
        else:

            # Appending the converted decimal octet
            first_host += str(int(first_host_octet, 2))
            last_host += str(int(last_host_octet, 2))
            
            # Stripping the leading octets
            first_host_bin = first_host_bin[8:]
            last_host_bin = last_host_bin[8:]

            # Clearing the temporary octet store for the next conversion
            first_host_octet = ""
            last_host_octet = ""
            
            continue
    

    

    

# This function will convert the network ID and broadcast into decimal notations
def calc_range(bin_net_id, bin_brdcst):

    global net_id
    global broadcast
    global net_id_octet
    global broadcast_octet

    net_id_octet = ""
    broadcast_octet = ""
    net_id = ""
    broadcast = ""

    for i in range(0,4):
        for binary in range(0,8):

            net_id_octet += bin_net_id[binary]
            broadcast_octet += bin_brdcst[binary]
        
        if i != 3:

            # Appending the converted decimal octet
            net_id += str(int(net_id_octet, 2)) + "."
            broadcast += str(int(broadcast_octet, 2)) + "."
            
            # Stripping the leading octets
            bin_net_id = bin_net_id[8:]
            bin_brdcst = bin_brdcst[8:]

            # Clearing the temporary octet store for the next conversion
            net_id_octet = ""
            broadcast_octet = ""
            
            continue
        else:

            # Appending the converted decimal octet
            net_id += str(int(net_id_octet, 2))
            broadcast += str(int(broadcast_octet, 2))
            
            # Stripping the leading octets
            bin_net_id = bin_net_id[8:]
            bin_brdcst = bin_brdcst[8:]

            # Clearing the temporary octet store for the next conversion
            net_id_octet = ""
            broadcast_octet = ""
            
            continue
    


# This function will iterate through the Binary IPv4 as many times as submask_counter of the user defined CIDR notation
# To get the Network ID
def calc_net_id(ipv4_bin, counter):

    global net_id_bin
    net_id_bin = ""

    for i in range(0, counter):

        net_id_bin += ipv4_bin[i]

    if len(net_id_bin) < 32:

        net_id_bin += "0" * ( 32 - len(net_id_bin))



# This function will iterate through the Binary IPv4 as many times as submask_counter of the user defined CIDR notation
# To get the Network ID
def calc_broadcast(ipv4_bin, counter):

    global broadcast_bin
    broadcast_bin = ""

    for i in range(0, counter):

        broadcast_bin += ipv4_bin[i]

    if len(broadcast_bin) < 32:

        broadcast_bin += "1" * ( 32 - len(broadcast_bin))




# Function for calculating the network ID, network range, broadcast, CIDR etc...
def calc_bin(ipv4, submask):

    global bin_submask
    bin_submask = ""

    global submask_counter
    submask_counter = 0

    if ipv4 and submask:
       
        # Binary IPv4
        bin_ipv4 = str('{0:08b}{1:08b}{2:08b}{3:08b}'.format( int(ipv4[0]), int(ipv4[1]), int(ipv4[2]), int(ipv4[3])  ))

        if len(submask) > 3:
            
            # Binary Subnet Mask ( Non CIDR )
            bin_submask = str('{0:08b}{1:08b}{2:08b}{3:08b}'.format( int(submask[0]), int(submask[1]), int(submask[2]), int(submask[3])  ))

            calc_net_id(bin_ipv4, sm_bin_converter(bin_submask))
            calc_broadcast(bin_ipv4, sm_bin_converter(bin_submask))
            
            # Calculating the first and last hosts binary values and passing the return values to the calc_hosts() function
            calc_hosts( *calc_hosts_bin(net_id_bin, broadcast_bin, sm_bin_converter(bin_submask) ) )
            submask_counter = sm_bin_converter(bin_submask)
    
        else:

            # This will determine the amount of times the calc_net_id() function will have to iterate through the bin_ipv4
            # in order to get the Network ID
            submask_counter = int(submask[0])
            calc_net_id(bin_ipv4, submask_counter)
            calc_broadcast(bin_ipv4, submask_counter)

            # Calculating the first and last hosts binary values and passing the return values to the calc_hosts() function
            calc_hosts( *calc_hosts_bin(net_id_bin, broadcast_bin, submask_counter ) )

    else:
        print("[ FATAL ERROR ] Aborting ...")
        sys.exit()




# Function to check user input validity
def check_input(ip, sm):

    user_input = [ip, sm]

    # Regex pattern for IPv4 input validation algorithm
    ip_regex_str = "([0-9]|1[0-9]{0,2}|[2-9][0-9]|2[0-4][0-9]|25[0-5])"
    
    # Regex pattern for CIDR input validation algorithm
    cidr_regex_str = "\\/([1-9]|1[0-9]|2[0-9]|3[0-2])"

    # Regex pattern for Subnet Mask input validation algorithm
    sm_regex_str = "(0|128|192|224|240|248|252|254|255)"

    # Applying the regex for IPv4, CIDR, and Subnet Mask respectfully 
    # The stored data type resolves to a <bool>
    ip_regex_result = re.search(f"^{ip_regex_str}\\.{ip_regex_str}\\.{ip_regex_str}\\.{ip_regex_str}$", user_input[0]) 
    cidr_regex_result = re.search(f"^{cidr_regex_str}$", user_input[1])
    sm_regex_result = re.search(f"^{sm_regex_str}\\.{sm_regex_str}\\.{sm_regex_str}\\.{sm_regex_str}$", user_input[1])


    if ip_regex_result and cidr_regex_result or sm_regex_result:

        print("Processing...")
        calc_bin( *splitter(user_input) ) # Return the user_input list to the splitter() function for further processing 

    else:
        print("\n[ ERROR ] Illegal input. Stopping program execution... [ ERROR ]")
        sys.exit()          # Stopping the program all together
            


# This function will gather all the information and print it to standard output
def print_info():

    print("\nIPv4 Address:",ip_input, end="\n\n")
    print("Network ID:", net_id, end="\n")
    print("Subnet Mask:", sm_input, end="\n")
    print("CIDR Notation:", submask_counter, end="\n")
    print("First Host:", first_host, end="\n")
    print("Last Host:", last_host, end="\n")
    print("Broadcast:", broadcast, end="\n")
    print("\nTotal Hosts:", ( 2 ** ( 32 - submask_counter ) ), end="\n")
    print("\nTotal Useable Hosts:", ( ( 2 ** ( 32 - submask_counter ) ) - 2 ), end="\n")
    



# Calling the check_input function with the return values from input_req() as arguments
# ' * ' unpacks the return values in their positional order 
check_input(*input_req())

calc_range(net_id_bin, broadcast_bin)

print_info()
