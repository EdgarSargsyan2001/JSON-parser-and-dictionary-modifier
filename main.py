from program import *

rF = open(FILENAME,"r")
readFileInfo = rF.readlines()
parsed_data = JSONParser(readFileInfo).parse()

if parsed_data == None:
    exit()


def foo():
    print('!dial "*" to finish')
    print('use "upd" to change')
    print('use "del" to delete')

    while True:
        command = input("Enter comand ") 
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








