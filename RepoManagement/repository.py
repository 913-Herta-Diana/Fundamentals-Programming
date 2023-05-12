import datetime

from domain import Reservation


class TextFileRepo():
    def __init__(self):
        self.__reservations = []

    def create(self,id_room,room_number,name,no_guests,arrival,departure,row,col):
        return Reservation(id_room,room_number,name,no_guests,arrival,departure,row,col)
    @property
    def reservations(self):
        return self.__reservations
    def __str__(self):
        return f'{self.__reservations}'
    def read_reservations(self):
        with open('reservations.txt', 'r') as fp:
            for line in fp:
                split_line = line[0:len(line) - 1].split(',')

                id = int(split_line[0])
                room_id = int(split_line[1])
                first_name = split_line[2]
                last_name = split_line[3]
                guests = int(split_line[4])
                split_arrival_date = split_line[5].split('-')
                arrival_date = datetime.date(int(split_arrival_date[0]), int(split_arrival_date[1]), int(split_arrival_date[2]))
                split_departure_date = split_line[6].split('-')
                departure_date = datetime.date(int(split_departure_date[0]), int(split_departure_date[1]), int(split_departure_date[2]))
                reservation = Reservation(id, room_id, room_id, first_name, last_name, guests, arrival_date, departure_date)
                self.__reservations.append(reservation)

        fp.close()




     # def display_available(self,arr,dep):
     #     for instance in self.__reservations:
     #         if arr>instance.__arrival:

    def delete(self,ide):
        for instance in self.__reservations:
            if instance.arrival==arr and instance.departure==dep:
                self.__reservations.remove(instance)
        with open("reservations.txt", "r") as f:
            lines = f.readlines()
        with open("reservations.txt", "w") as f:

            for line in lines:
                split_line = line[0:len(line) - 1].split(',')
                if int(split_line[0]) != ide:
                    f.write(line)
        f.close()
    def delete_interval(self,res,arr,dep):
        if (res.arrival> arr and res.arrival<dep):
            self.__reservations.remove(res)
            print(self.__reservations)






arr="2023-10-03"
dep="2023-10-05"
r=TextFileRepo()




