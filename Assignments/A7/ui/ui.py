from src.services.services import Service
from src.domain.domain import Expense

class UserInterface:
    def __init__(self):
        self.srv=Service()
        self.commands={
            'add': self.add_expense,
            'display': self.list_expenses,
            'filter': self.filter_expenses,
            'undo': self.undo
        }
    def add_expense(self):
        """
        :return: Adds a new expense to the list
        """
        day=self.check_day(input("Day: "))
        amount=self.check_amount(input("Amount: "))
        type=input("Type: ")

        expense=Expense(day,amount,type)
        try:
            self.srv.addition(expense)
        except Exception as ex:
            print(str(ex))
    def list_expenses(self):
        print(self.srv.displaying())
    def filter_expenses(self):
        value=int(input("Show expenses lesser than "))
        print(self.srv.filtering(value)) #da offsetu in loc de valori
    def undo(self):
        try:
            self.srv.hopefully_undo()
        except Exception as ex:
            print(str(ex))
    def handling_input(self):
        option = input("What should I do?\n")
        if option in self.commands:
            self.commands[option]()
        else:
            print("Command not recognized.")
    def check_day(self,day):
        while True:
            try:
                assert day.isdigit()
                assert int(day) > 0 and int(day) < 31
                break
            except:
                print(f"Oops! Day {day} doesn't exist!")
                self.add_expense()
        return int(day)

    def check_amount(self,amount):

        while True:
            try:
                assert amount.isdigit()
                assert int(amount) > 0
                break
            except:
                print(f"Oops! You can't pay this amount")
                self.add_expense()


        return int(amount)
def print_menu():
    print('1. Add an expense')
    print('2. Display all expenses' )
    print('3. Filter greater than')
    print('4. Undo')