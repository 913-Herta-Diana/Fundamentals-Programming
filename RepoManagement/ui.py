class UI:
    def __init__(self,service):
        self.__service=service
    @staticmethod
    def print_menu():
        message="Hotel management.\n1.Check available rooms\n2.Make a reservation" \
                "\n3.Delete reservation\n4.Delete reservation between dates\n5.Monthly report\n" \
                "6.Display reservations\n7.Create month table\n0.exit"
        print(message)

    def start_menu(self):
        commands=['1','2','3','4','5','6','7']

        while True:
            UI.print_menu()
            command = input("Choose an option: ")
            if command not in commands:
                command=input("Choose a valid option: ")
            if command=='0':
                break
            if command=='1':
                arr=input("Insert arrival date: ")
                dep=input("Insert departure date: ")
                self.__service._display_available(arr,dep)
            if command=='2':
                self.__service._make_res()
            if command=='3':
                ide=int(input("Input nr: "))
                self.__service._delete_res(ide)
            if command=='4':
                arr=input("Arrival date: ")
                dep=input("Departure date: ")
                self.__service._delete_dates(arr,dep)
            if command=='5':
                print(self.__service._monthly_rep())
            if command=='6':
                self.__service._display_res()
            if command=='7':
                self.__service._month_table()

