class Service:
    def __init__(self):
        self._expenses_list=[]

    @property
    def expenses(self):
        return self._expenses_list

    @expenses.setter
    def students(self, new_list):
        self._expenses_list = new_list

    def add_expense(self, expense):
        self._expenses_list.append(expense)

    def filter_expenses(self, value, list):
        """
        Implements the filter command.
        :param command: string
        """
        new_list=[]
        for obj in list:
            if amount(obj)<value:
                new_list.append(obj)
        return new_list




