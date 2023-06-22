from functions import *
import os

if not os.path.isfile(os.getcwd() + "/" + FILENAME): # if input file there isn't any we create it and writing empty object {}
    path = os.path.join((os.getcwd()), FILENAME)
    f = open(FILENAME, "w")
    f.write("{}")
    f.close()

rF = open(FILENAME, "r")  # read from input file
parsed_data = JSONParser(rF.read()).parse()  # pares JSON string to dictionary

if parsed_data == None:  # if parser failed to parse
    exit()


def foo():
    print('!use "*" to finish')
    print('!use "upd" to change')
    print('!use "del" to delete')

    while True:
        print(object_to_string(parsed_data))  # print each iteration parsed data
        command = input("\nEnter comand ")
        keyword = command[0:3]
        isSaved = False

        if command == "*":
            break
        elif keyword == "del":
            isSaved = delete_in_dictionary(parsed_data, command[3:])
        elif keyword == "upd":
            isSaved = change_in_dictionary(parsed_data, command[3:])
        else:
            isSaved = add_in_dictionary(parsed_data, command)

        if isSaved:
            save_object_in_file(parsed_data, FILENAME)  # save object in file

foo()
