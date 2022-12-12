#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 

from ui import *
import operator
#got it
def create_dictionary(day, value, type, description):
    return {'day': day, 'value': value, 'type': type, 'description': description}

def test_add():
    try:
        assert add([{'day': 2, 'value': 15,'type': 'in', 'description': 'pizza'},{'day': 3, 'value':12,'type': 'out', 'description': 'food' }],3,2,'out','makeup')==[{'day': 2, 'value':15,'type': 'in', 'description': 'pizza'},{'day': 3, 'value':12,'type': 'out', 'description': 'food', },{'day': 3, 'value':2,'type': 'out', 'description': 'makeup'}]
        pass
    except:
        print("Function doesn't work well!add")

def test_insert():
    try:
        assert insert([{'day': 2, 'value': 15,'type': 'in', 'description': 'pizza'},{'day': 3, 'value':12,'type': 'out', 'description': 'food'}], 3, 200, 'in', 'heels')==[{'day': 2, 'value': 15,'type': 'in', 'description': 'pizza'},{'day': 3, 'value':200,'type': 'in', 'description': 'heels'}]
        pass
    except:
        print("Function doesn't work well!insert")
def test_remove_day():
    try:
        assert remove([{'day': 2, 'value': 15,'type': 'in', 'description': 'pizza'},{'day': 3, 'value':12,'type': 'out', 'description': 'food' }],2)==[{'day': 3, 'value':12,'type': 'out', 'description': 'food'}]
        pass
    except:
        print("Function doesn't work wellremove day!")
def test_remove_start_to_end():
    try:
        assert remove_start_to_end([{'day': 2, 'value': 15,'type': 'in', 'description': 'pizza'},{'day': 3, 'value':12,'type': 'out', 'description': 'food' }],2,3)==[]
        pass
    except:
        print("Function doesn't work well!start")

def test_remove_type():
    try:
        assert remove_category([{'day': 2, 'value': 15,'type': 'in', 'description': 'pizza'}],'in')==[]
        pass
    except:
        print("Function doesn't work welltype!")

def test_replace():
    try:
        assert replace_a_lot([{'day': 2, 'value': 15,'type': 'in', 'description': 'pizza'}],2,'in',200,"pizza")==[{'day': 2, 'value': 200,'type': 'in', 'description': 'pizza'}]
        pass
    except:
        print("Function doesn't work wellreplace!")
def add(list,day,value,type,description):
    """

    :param list: all the transactions
    :param value: the amount of money
    :param type: in or out transaction
    :param description: the product
    :return: adds the new transaction add
    """
    list.append(create_dictionary(day,value,type,description))
    return list

def insert(list,day,value,type,description):
    """

    :param list: all the transactions

    :param value: the amount of money
    :param type: in or out transaction
    :param description: the products
    :return: inserts a new transaction in the specified day
    """
    k=0
    for dictionary in list:
        if get_date(dictionary)==day:
            dictionary.update(
                {
                    "value": value,
                    "type": type,
                    "description": description
                }
            )
            k=1
    if k==1:
        return list
    else:
        list.append(create_dictionary(day, value, type, description))
        return list

def remove(list,day):
    """

    :param list: all the transactions
    :param day: the day of the transaction
    :return: removes the transaction from the specified day
    """
    n=len(list)
    i=0
    while i<n:
        if day==get_date(list[i]):
            del list[i]
            n-=1
        else:
            i+=1
    return list
def remove_start_to_end(list,start_date,end_date):
    '''

       :param start_date: a positive integer representing the day from which the transactions will be removed
       :param end_date: a positive integer representing the day where removal of the transactions will stop
       :return: the function returns the list with deleted transactions between the starting day and the ending day
       '''
    list.sort(key=operator.itemgetter("day"))
    print(list)
    n = len(list)
    i = 0
    while i < n:
        if get_date(list[i]) >= start_date and get_date(list[i]) <= end_date:
            del list[i]
            n-=1
        else:
            i += 1
    return list
def remove_category(list,type):
    """
        :param list: all the transactions
        :param type: in or out transaction
        :return: removes the transaction with the specified type
        """
    i=0
    n=len(list)
    while i<n:
        if get_type(list[i])==type:
            del list[i]
            n-=1
        else:
            i+=1
    return list
def replace_a_lot(list,day,type,amount,description):
    """

    :param list: all the transactions
    :param  day: the day of the transaction
    :param type: in or out transaction
    :param amount: the value of money
    :param description: product
    :return: replaces the value of the transaction with specified day, type and description
    """
    for dictionary in list:
        if day==get_date(dictionary):
            if type==get_type(dictionary):
                if description==get_description(dictionary):
                    dictionary.update(
                        {
                            "value": amount}
                    )
    return list

def list_all(dictionary):
    """

    :param dictionary: a transaction
    :return: the transaction
    """
    return dictionary

def list_type(list,type):
    """

    :param list: list of transactions
    :param type: type of transactions
    :return: only the transactinos with speficied type
    """
    new_list=[]
    for dictionary in list:
        if type == get_type(dictionary):
            new_list.append(dictionary)
    return new_list

def list_operator(list,amount, operator):
    """

    :param list: list of transactions
    :param amount: amount of money
    :param operator: operator for comparing
    :return: list of transactions with values that respect the condition implied by the operator
    """
    new_list=[]
    for i in range(len(list)):
        if operator=='>':
            if get_value(list[i]) > amount:
                new_list.append(list[i])
        elif operator=="=":
            if get_value(list[i]) == amount:
                new_list.append(list[i])
        elif operator=='<':
            if get_value(list[i]) < amount:
                new_list.append(list[i])
    return new_list

def list_balance(list,day):
    """

    :param list: list of transactions
    :param day: the date of the transaction
    :return: the balance at the day of the transaction
    """
    sum_in=0
    sum_out=0
    for dictionary in list:
        if get_date(dictionary)<=day:
            if get_type(dictionary)=='in':
                sum_in+=get_value(dictionary)
            else:
                sum_out+=get_value(dictionary)
    return sum_in-sum_out
def filter(list,type):
    """

    :param list: list of transactions
    :param type: type of  transaction
    :return: filters the transactions with speficied type
    """
    n=len(list)
    i=0
    while i<n:
        if get_type(list[i])!=type:
            del list[i]
            n-=1
        else:
            i+=1
    return list
def filter_lesser_than(list,type,amount):
    """

    :param list: list of transactions
    :param type: type of transaction
    :param amount: amount of money
    :return: filters the transactions with specified type and with a value lesser than the amount
    """
    n = len(list)
    i = 0
    while i < n:
        if get_type(list[i]) != type or get_value(list[i])>=amount:
            del list[i]
            n -= 1
        else:
            i += 1
    return list
def create_stack(stack,list):
    stack.append(list)
    return stack
def get_date(account):
    return int(account["day"])
def get_value(account):
    return int(account["value"])
def get_type(account):
    return str(account['type'])
def get_description(account):
    return account['description']
def set_date(account,day):
    account['day'] = day
    return account['day']
def set_value(account,value):
    account['value'] = value
    return account['value']
def set_type(account,type):
    account['type'] = type
    return account['type']
def set_description(account,description):
    account['description'] = description
    return account['description']
