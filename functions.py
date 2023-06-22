from parser_1 import *

FILENAME = "objectFile.txt"


def is_str_int(var):
    try:
        int(var)
    except ValueError:
        return False
    return True


def save_object_in_file(obj, filename):
    string = object_to_string(obj)
    writeFile = open(filename, "w")
    writeFile.write(string)
    writeFile.close()


def add_in_dictionary(obj, comand):
    comand = comand.split(".")  # split enter comand ex. k.m = 44 -> ["k","m = 44"]
    i = 0
    while i < len(comand) - 1:  # search object
        if comand[i] in obj:
            obj = obj[comand[i]]
        else:
            print("Warning: invalid key 1")
            return
        i += 1

    if type(obj) != dict:  # if it isn't object return
        print("Warning: " + comand[-2] + " value is not object")
        return

    arr = comand[-1].replace(" ", "").split("=")  # split the last command
    if len(arr) != 2:  # that length must be 2 ex.   ["key","value"]
        print("Warning: invalid key 2")
        return

    key = arr[0]
    value = arr[1]
    if key in obj:  # if key in a object return
        print("Warning: key already has in a object")
        return

    if is_str_int(value):  # if value is integer
        value = int(value)
    elif "{" in value and "}" in value:  # if value is object use JSONparser
        try:
            value = JSONParser(value).parse_value()
        except:
            value = None

    if value == None:  #  if value is None
        print("Warning: invalid value")
        return

    obj[key] = value  # everything is ok we can set value in object
    return True


def change_in_dictionary(obj, comand):
    comand = comand.replace(" ", "").split(".")    # split enter comand ex. upd k.m = 44 -> ["k","m = 44"]

    i = 0
    while i < len(comand) - 1:  # search object
        if comand[i] in obj:
            obj = obj[comand[i]]
        else:
            print("Warning: invalid key for changing")
            return
        i += 1

    arr = comand[-1].split("=")  # split the last command
    if len(arr) != 2:  # that length must be 2 ex.   ["key","value"]
        print("Warning: invalid key for changing")
        return

    key = arr[0]
    value = arr[1]

    if is_str_int(value):  # if value is integer
        value = int(value)

    elif "{" in value and "}" in value:
        try:
            value = JSONParser(value).parse_value()
        except:
            value = None

    if value == None:
        print("Warning: invalid value")
        return
    obj[key] = value  # everything is ok we can set value in object
    return True


def delete_in_dictionary(obj, comand):
    comand = comand.replace(" ", "").split( ".")  # split enter comand ex. del k.m  -> ["k","m"]
       
    i = 0
    while i < len(comand) - 1:  # search object
        if comand[i] in obj:
            obj = obj[comand[i]]
            # key = comand[i]
        else:
            print("Warning: invalid key for deleting")
            return
        i += 1

    key = comand[-1] # key is last element of comand
    if key not in obj:# if key isn't object return
        print("Warning: Invalid key for deleting")
        return
    
    obj = obj.pop(key)
    return True

