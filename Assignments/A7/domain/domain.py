import random
class Expense:
    def __init__(self,day,amount,type):
        self.__day = day
        self.__amount = amount
        self.__type = type

    def __str__(self):
        return f"On day {self.day} you paid {self.__amount} for this product {self.__type}"

    def __repr__(self):
        return f"On day {self.day} you paid {self.__amount} for this product {self.__type}"

    # Getters
    @property
    def day(self):
        return self.__day

    @property
    def amount(self):
        return self.__amount

    @property
    def type(self):
        return self.__type

    # Setters
    @day.setter
    def day(self, new_day):
        self.__day = new_day

    @amount.setter
    def amount(self, new_amount):
        self.__amount = new_amount

    @type.setter
    def type(self,new_type):
        self.__type=new_type

    # Predefined
list_of_types = ["food", "clothes", "cleaning tools","magazines","car","shoes","cosmetics"]


def rand_day():
    day=random.randint(1,30)
    return day
def rand_amount():
    amount=random.randint(1,100000)
    return amount

def rand_type():
    type=random.randint(0,len(list_of_types)-1)
    return type

def rand_expenses():
    expenses=[]
    for i in range(1,11):
        expense=Expense(rand_day(),rand_amount(),rand_type())
        expenses.append(expense)
    return expenses

