from texttable import Texttable


class Reservation:
    def __init__(self, reservation_id:int, room_id:int, room_number:int, first_name:str, last_name:str, guests:int, arrival, departure):
        self.__reservation_id = reservation_id
        self.__room_id=room_id
        self.__room_number=room_number
        self.__first_name=first_name
        self.__last_name=last_name
        self.__guests=guests
        self.__arrival=arrival
        self.__departure=departure

    def __str__(self):
        return f'id = {self.__reservation_id}, room_id = {self.__room_id}, room_number = {self.__room_number}, first_name = {self.__first_name}, last_name = {self.__last_name}, guests = {self.__guests}, arrival = {self.__arrival}, departure = {self.__departure}'
    @property
    def guests(self):
        return self.__guests
    @property
    def first_name(self):
        return  self.__first_name
    @property
    def reservation_id(self):
        return self.__reservation_id
    @property
    def arrival(self):
        return self.__arrival

    @arrival.setter
    def arrival(self, value):
        self.__arrival=value

    @property
    def departure(self):
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure=value


