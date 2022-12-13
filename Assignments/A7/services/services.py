from src.domain.domain import rand_expenses
from src.domain.domain import Expense

class Service:
    def __init__(self,init_rand=True):
        self.expenses=rand_expenses() if init_rand else []
        self.undo=[]
    def duplicates(self,expense):
        def same_type(b):
            return b.type==expense.type
        return any(map(same_type, self.expenses))

    def addition(self,expense):
        """

        :param expense: expense that needs to be added
        :return: adds expense to the list
        """
        if self.duplicates(expense):
            raise Exception("Expense already exists")
        self.undo.append(self.expenses.copy())
        self.expenses.append(expense)
    def displaying(self):
        return '\n'.join(map(str,self.expenses))
    def filtering(self,value):
        def is_greater_than(s):
            return s.amount > value #la filter fix aici
        self.expenses=list(filter(is_greater_than,self.expenses))
        self.undo.append(self.expenses)
        return self.expenses


    def hopefully_undo(self):
        if not self.undo:
            return False
        self.expenses=self.undo.pop()
        return True
