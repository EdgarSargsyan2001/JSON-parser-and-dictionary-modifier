from parser_1 import *
FILENAME = "objectFile.txt"

def is_str_int(var):
    try:
        int(var)
    except ValueError:
        return False
    return True

def save_data_in_file(obj,filename):
    string = object_to_string(obj)
    writeFile = open(filename,"w")
    writeFile.write(string)
    writeFile.close()

def add_in_dictionary(parsed_data_obj,comand):
    comand = comand.split('.')
    obj = parsed_data_obj
    i = 0
    while i < len(comand)-1:
        if comand[i] in parsed_data_obj:
            obj = parsed_data_obj[comand[i]]
        else:
            print("Warning: invalid key")
            return
        i+=1
    
    arr = comand[-1].replace(' ','').split('=')
    if len(arr) != 2:
        print("Warning: invalid key")
        return
    
    key = arr[0]
    value = arr[1]
    if key in obj:
        print('Warning: key already has in a object')
        return
    
    parseValue = value
    if is_str_int(value):
        parseValue = int(value)
    elif '{' in value:
        parseValue = JSONParser(value).parse_value()
    
    if parseValue == None:
        print("Warning: invalid value")
        return
    obj[key] = parseValue


def change_in_dictionary(parsed_data_obj,comand):
    comand = comand.replace(' ','').split('.')
    obj = parsed_data_obj
    i = 0
    while i < len(comand)-1:
        if comand[i] in parsed_data_obj:
            obj = parsed_data_obj[comand[i]]
        else:
            print("Warning: invalid key for changing")
            return
        i+=1
    
    arr = comand[-1].split('=')
    if len(arr) != 2:
        print("Warning: invalid key for changing")
        return
    
    key = arr[0]
    value = arr[1]
    parseValue = value
    if is_str_int(value):
        parseValue = int(value)
    elif '{' in value and '}' in value:
        parseValue = JSONParser(value).parse_value()
    
    if parseValue == None:
        print("Warning: invalid value")
        return
    obj[key] = parseValue



def delete_in_dictionary(parsed_data_obj,comand):
    comand = comand.replace(' ','').split('.')
    i = 0
    while i < len(comand) - 1 : 
        if comand[i] in parsed_data_obj:
            parsed_data_obj = parsed_data_obj[comand[i]]
            key = comand[i]
        else:
            print("Warning: invalid key for deleting")
            return
        i+=1
    key = comand[-1]
    if key in parsed_data_obj:
        parsed_data_obj = parsed_data_obj.pop(key)
        return
    else:
        print('Warning: Invalid key for deleting')
        return
    