#!/usr/bin/python3

## for "How to check if a line has one of the strings in a list? [duplicate]"
# https://stackoverflow.com/questions/8583615/how-to-check-if-a-line-has-one-of-the-strings-in-a-list

"""
strings = ("string1", "string2", "string3")
for line in file:
    if any(s in line for s in strings):
        print "yay!"
"""

"""
>>> lines1 = ['soup', 'butter', 'venison']
>>> lines2 = ['prune', 'rye', 'turkey']
>>> search_strings = ['a', 'b', 'c']
>>> any(s in l for l in lines1 for s in search_strings)
True
>>> any(s in l for l in lines2 for s in search_strings)
False
"""

##

##  large file navigation, but it does bytes, not strings
# https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files

## How to Read Extremely Large Text Files Using Python
# https://code.tutsplus.com/quick-tip-how-to-read-extremely-large-text-files-using-python--cms-25992t
"""
with open('hg38.txt','r') as input_file:
    while(1):
        for lines in range(50):
            print(input_file.readline())
        user_input = input('Type STOP to quit, otherwise press the Enter/Return key ')
        if user_input == 'STOP':
            break
"""

## Python Program to Print Lines Containing Given String in File
# https://www.geeksforgeeks.org/python-program-to-print-lines-containing-given-string-in-file/

## Read content from one file and write it into another file
# https://www.geeksforgeeks.org/read-content-from-one-file-and-write-it-into-another-file/

with open('20250202_1700__show_configuration_commands.txt','r') as input_file:
    w_a_write_access = "w"
    #w_a_write_access = "a"
    with open("temp_holding_mappings.txt", w_a_write_access) as temp:
        temp.write( "entry" )
        temp.write( "\n" )
        temp.write( "\n" )
#        while(1):
#            for lines in range(25):
#                line = input_file.readline()
        for line in input_file:
            if "static-mapping" in line:
                #print( line )
                temp.write( line )

with open('temp_holding_mappings.txt','r') as temp:
    w_a_write_access = "w"
    #w_a_write_access = "a"
    with open("reserved_dhcp__from_edgerouter.txt", w_a_write_access) as output_file:
        for line in temp:
            if "static-mapping" in line:
# set service dhcp-server shared-network-name LAN_ALL subnet 192.168.5.0/24 static-mapping NetworkCloset-UACpro ip-address 192.168.5.52

                data_dictionary = {}
                raw_data = line.partition( "static-mapping" )
                this_part = raw_data[0].partition( "set service dhcp-server shared-network-name" )[2].partition( "subnet" )
                data_dictionary["network_name"] = this_part[0].strip()
                data_dictionary["subnet"] = this_part[2].strip()
                #print( raw_data[2].split() )
                data_dictionary["name"], data_dictionary["address_type"], data_dictionary["address"] = raw_data[2].split()

                #data_dictionary["name"] = raw_data[2][0].split(" ")
                #data_dictionary["address_type"] = raw_data[2][1].split(" ")
                #data_dictionary["address"] = raw_data[2][2].split(" ")

                '''
                               if data_dictionary["address_type"] is not "mac-address":
                                   if data_dictionary["address_type"] is not "ip-address":
                                       print(data_dictionary["address_type"])
                                       print("    poooooop")
                '''
                #print("address_type:  ", data_dictionary["address_type"])


                data_dictionary["ip_address"] = data_dictionary["address"]
                data_dictionary["mac_address"] = data_dictionary["address"]
                data_dictionary["issue_to_handle"] = True

                #.strip()
                for item in data_dictionary.values():
                    output_file.write(item.strip())
                    output_file.write(" ")
                output_file.write("\n")
                #print( line )
                #output_file.write( line )

                if data_dictionary["address_type"]:

'''
                match data_dictionary["address_type"]:
                    case "ip-address":

                    case "mac-address":

                    case _:



                if data_dictionary["address_type"] != any(["mac-address", "ip-address"]):
                    print("    " + data_dictionary["address_type"])
                    print("    poooooop")
'''
'''
with open('temp_holding_mappings.txt','r') as input_file:
    #with open("temp_holding_mappings.txt", "w") as temp:
    with open("mappings.csv.txt", "a") as temp:
        temp.write( "enty" )
        while(1):
            for lines in range(25):
                line = input_file.readline()
                if "static-mapping" in line:
                    print( line )
                    temp.write( line )
'''



#for line in file:
#    if line.find("static-mapping") not equal (-1):

