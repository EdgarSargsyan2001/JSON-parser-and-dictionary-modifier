from random import randrange
from program import JSONParser ,change_in_dictionary,add_in_dictionary,delete_in_dictionary,save_data_in_file
from parser_1 import object_to_string
import os

TESTCOUNT = 10

def make_folder(name,path = ''):
    if not os.path.isdir(os.getcwd() + path ):
        path = os.path.join((os.getcwd() + path ), name)
        os.makedirs(path)
    

def append_inst_arr_in_file(arr,filename):
    writeFile = open(filename,"a")
    writeFile.write('\n'+str(arr)+'\n')
    writeFile.close()

def append_dictionary_in_file(obj,filename):
    string = object_to_string(obj)
    writeFile = open(filename,"a")
    writeFile.write(string)
    writeFile.close()

def creat_random_object():

    arrObjectsKey = ["student","school","Armenia","Erevan","book","python"]
    arrObjectsValue = [44,{"age":2000},{"info":{"a":44,"b":33}},"Programiz",
                   {
                        "United States": "Washington D.C.", 
                        "Italy": "Rome", 
                        "England": "London"
                    }
                   ]
    randomOBJ = {}

    for i in range(5):
        randomOBJ[arrObjectsKey[randrange(0,6)]] = arrObjectsValue[randrange(0,5)]

    return randomOBJ

def creat_random_instruction(obj):
    arrkey = list(obj.keys())
    arrinstruction = ['del' ,'upd','add']
    arrvalue = ['programmer',44 , "bold",{"id": "file"},{
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    }]
    arraddkey = ['hOffset',"vOffset","alignment","servlet-name"]
    instructionSize = 4
    arr = []
    
    for i in range(instructionSize):
        inst = arrinstruction[randrange(0,len(arrinstruction))]
        key = arrkey[randrange(0,len(arrkey))]
        value = arrvalue[randrange(0,len(arrvalue))]
        addkey = arraddkey[randrange(0,len(arraddkey))]

        if inst == 'add':
            arr.append({"i":inst,"k":addkey,'v':value})
        elif inst == 'upd':
            arr.append({"i":inst,"k":key,'v':value})
        else:
            arr.append({'i':inst,'k':key,'v':None})
    return arr



def do_actions_with_the_real_object(instArr,obj):
    for el in instArr:
        key = el['k']
        inst = el['i']
        val = el['v']

        if inst == 'upd':
            obj[key] = val
        elif inst == 'add' and key not in obj:
            obj[key] = val
        elif  inst == 'del' and key in obj:
            obj.pop(key)


def do_actions_by_my_rules(instArr,obj):
    for el in instArr:
        key = el['k']
        inst = el['i']
        val = str(el['v'])

        if inst == 'upd':
            change_in_dictionary(obj, (key +'=' + val))
        elif inst == 'add':
            add_in_dictionary(obj, (key +'=' + val))
        elif  inst == 'del' and key in obj:
            delete_in_dictionary(obj,key )

make_folder("Tests")
make_folder("Ans",'/Tests')

ansArr = []
def foo(index):
    TestfileN = './Tests/test'+str(index)+'.txt'
    AnsfileN = './Tests/Ans/ans'+str(index)+'.txt'
    rObj = creat_random_object()
    save_data_in_file(rObj,TestfileN)

    instArr = creat_random_instruction(rObj)

    do_actions_with_the_real_object(instArr,rObj)

    rF = open(TestfileN,"r")
    parsed_data = JSONParser(rF.readlines()).parse()
    do_actions_by_my_rules(instArr,parsed_data)

    writeFile = open(AnsfileN,"w")
    writeFile.write(str(instArr)+"\n\n")
    writeFile.close()

    a = str(rObj).replace(' ','')
    b =str(parsed_data).replace(' ','')
    append_dictionary_in_file(parsed_data,AnsfileN)
    append_inst_arr_in_file(a == b,AnsfileN)
    ansArr.append(a == b)
    index +=1
    return a == b


saveAnsFile = open("./Tests/Test answer.txt","w")

for i in range(TESTCOUNT):
    print("index: ",i ,"  is " ,foo(i))
    saveAnsFile.write("index: " + str(i) + "  is " + str(ansArr[i]) + '\n')


saveAnsFile.close()

