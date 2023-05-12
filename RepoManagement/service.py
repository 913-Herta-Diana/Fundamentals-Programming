import datetime

from texttable import Texttable


class Service:
    def __init__(self, repo):
        self._repo = repo
        self._repo.read_reservations()
    def _delete_res(self,ide):
        self._repo.delete(ide)
    def _delete_dates(self,arr,dep):
        arr=arr.split(".")
        dep=dep.split(".")
        arrival=datetime.date(2023,int(arr[0]),int(arr[1]))
        departure=datetime.date(2023,int(dep[0]),int(dep[1]))
        for res in self._repo.reservations:
            self._repo.delete_interval(res,arrival,departure)
    def _monthly_rep(self):
        def dis(el):
            return el.arrival
        display=[]
        for res in self._repo.reservations:
            #if some condition
            display.append(res)
        display.sort(key=dis, reverse=False)
        firstMonth = display[0].arrival.month
        lastMonth = display[-1].arrival.month
        Month=firstMonth
        MonthDate= datetime.date(2023,Month,1)
        index=0
        string=""
        while Month<lastMonth:
            table=Texttable()
            table.header([MonthDate.strftime("%B"),"Name","Guests"])
            while index<len(display) and display[index].arrival.month == Month:
                table.add_row([f"{display[index].arrival.strftime('%m.%d')}-{display[index].departure.strftime('%m.%d')}",str(display[index].first_name),f"{display[index].guests} person(s)"])
                index+=1
            string += table.draw() + "\n\n"
            Month+=1
            MonthDate= datetime.date(2023, Month, 1)

        return string




