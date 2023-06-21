from functions import *
import os

if not os.path.isfile(os.getcwd() + "/" + FILENAME):
    path = os.path.join((os.getcwd()), FILENAME)
    f = open(FILENAME, "w")
    f.write('{}')
    f.close()

rF = open(FILENAME, "r")
print(rF)
readFileInfo = rF.readlines()
parsed_data = JSONParser(readFileInfo).parse()

if parsed_data == None:
    exit()


def foo():
    print('!use "*" to finish')
    print('!use "upd" to change')
    print('!use "del" to delete')

    while True:
        print( object_to_string(parsed_data) )
        command = input("\nEnter comand ")
        keyword = command[0:3]
        if command == '*':
            break
        elif keyword == 'del':
            delete_in_dictionary(parsed_data,command[3:])
        elif keyword == 'upd':
            change_in_dictionary(parsed_data,command[3:])
        else :
            add_in_dictionary(parsed_data,command)
        save_data_in_file(parsed_data,FILENAME)


foo()
