#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
from __future__ import print_function
from functions import *
from datetime import datetime
import copy


def print_list(list):
    for i in list:
        print(i)
def print_menu():
    print('1. add <value> <type> <description>')
    print('2. insert <day> <value> <type> <description>')
    print('3. remove <day>')
    print('4. remove <start day> to <end day>')
    print('5. remove <type>')
    print('6. replace <day> <type> <description> with <value>')
    print('7. list')
    print('8. list <type>')
    print('9. list [ < | = | > ] <value>')
    print('10. list balance <day>')
    print('11. filter <type>')
    print('12. filter <type> <value>')
    print('13. undo ')
    print('14. exit\n')
def create_dictionary(day, value, type, description):
    return {"day": day, "value": value, "type": type, "description": description}
def split_and_lower_words(option):
    for i in range(len(option)):
        option[i]=option[i].lower()
    return option
def run_menu():
    data = []
    stack=[]
    undo_data=[]
    data.append(create_dictionary(2, 18, "in", "pizza"))
    data.append(create_dictionary(2, 15, "out", "pizza"))
    data.append(create_dictionary(2, 18, "in", "pizza"))
    data.append(create_dictionary(4, 13, "in", "pizza"))
    data.append(create_dictionary(5, 8, "in", "pizza"))
    data.append(create_dictionary(29, 7, "out", "burger"))
    data.append(create_dictionary(6, 15, "in", "pizza"))
    data.append(create_dictionary(7, 15, "in", "pizza"))
    data.append(create_dictionary(10, 21, "in", "shoes"))
    running = True

    while running:
        print_menu()
        option = input("Tell me what to do: ")
        option=split_and_lower_words(option.split())
        use_in_undo=True
        try:
            if option[0]=="add" and len(option)==4:
                menu_add(data,option)
            elif option[0] == "insert" and len(option)==5:
                menu_insert(data,option)
            elif option[0]=="remove":
                if len(option)==2:
                    if(option[1].isdigit()):
                        menu_remove_day(data, option)
                    else:
                        menu_remove_type(data,option)
                elif option[2]=="to":
                    menu_remove_start_end(data,option)
                    #TO,WITH PB
            elif option[0]=="replace" and len(option)==6:
                menu_replace(data,option)
            elif option[0]=="list":
                use_in_undo = False
                if len(option)==1:
                    menu_list(data)
                elif len(option)==2:
                    menu_list_type(data, option)
                else:
                    if option[1]=="balance":
                        menu_list_balance(data,option)
                    elif option[1]=='<' or option[1]=='>' or option[1]=='=':
                        menu_list_compare(data,option)
            elif option[0]=="filter":
                if len(option)==2:
                    menu_filter(data, option)
                else:
                    menu_filter_value(data,option)
            elif option[0]=="undo" and len(option)==1:
                use_in_undo=False
                print(stack.pop())
                stack=copy.deepcopy(stack)
                for list in stack:
                    undo_data=list
                data=copy.deepcopy(undo_data)
            elif option[0]=="exit" and len(option)==1:
                print("Adios")
                running = False
                use_in_undo=False
            else:
                print("Be careful with what you input!")
            if use_in_undo==True:
                create_stack(stack,copy.deepcopy(data))
        except Exception as e:
            print("You should type something!")


def menu_add(list,option):
    value=check_value(option[1])
    type=check_type(option[2])
    description=check_description(option[3])
    add(list,datetime.now().day,value,type,description)

def menu_insert(list, option):
    day=check_day(option[1])
    value=check_value(option[2])
    type=check_type(option[3])
    description=check_description(option[4])
    insert(list,day,value,type,description)

def menu_remove_day(list, option):
    day=check_day(option[1])
    remove(list,day)
def menu_remove_start_end(list, option):
    start_day=check_day(option[1])
    end_day=check_day(option[3])
    remove_start_to_end(list,start_day,end_day)
def menu_remove_type(list, option):
    type=check_type(option[1])
    remove_category(list,type)
def menu_replace(list, option):
    day=check_day(option[1])
    type=check_type(option[2])
    description=check_description(option[3])
    value=check_value(option[5])
    replace_a_lot(list,day,type,value,description)

def menu_list(list):
    for dictionary in list:
        print(list_all(dictionary))
def menu_list_type(list,option):
    type=check_type(option[1])
    print(*list_type(list,type),sep='\n')
def menu_list_compare(list, option):
    operator=check_operator(option[1])
    amount=check_value(option[2])

    print(*list_operator(list,amount,operator),sep='\n')
def menu_list_balance(list, option):
    day=check_day(option[2])
    print(list_balance(list,day))
def menu_filter(list, option):
    type=check_type(option[1])
    filter(list,type)
def menu_filter_value(list, option):
    type=check_type(option[1])
    value=check_value(option[2])
    filter_lesser_than(list,type,value)

def check_day(day):
    while True:
        try:
            assert day.isdigit()
            assert int(day)>0 and int(day)<31
            break
        except:
            print("Oops!That was not a natural number.  Try again...")
            run_menu()
    return int(day)
def check_value(value):


    while True:
        try:
            assert value.isdigit()
            assert int(value)>0
            break
        except:
            print("Oops!  That was not a natural number.  Try again...")
            run_menu()

    return int(value)
def check_type(type):
    while True:
        try:
            assert type=='in' or type=='out'
            break
        except:
            print("Oops! Impossible type of transaction.  Try again...")
            run_menu()
    return type
def check_description(description):
    return description
def check_operator(operator):
    while True:
        try:
            assert operator == '<' or operator == '>' or operator == '='
            break
        except:
            print('Wrong input! Insert one of the operators <,=,>.')
            run_menu()
    return str(operator)