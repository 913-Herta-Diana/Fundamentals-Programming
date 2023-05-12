from board import Board
from player import Player



class UI:
    def __init__(self,service):
        self._service=service
    @staticmethod
    def print_menu():
        message="Loading snake...\n1.Start game\n0.Exit"
        print(message)
    @staticmethod
    def print_submenu():
        message="a. move\nb. change position\n"
        print(message)
    def _start(self):
        commands1=['1','0']
        commands2=['a','b']
        self.print_menu()
        command1 = input("Choose an option: ")
        while True:
            try:
                while command1 not in commands1:
                    command1=input("Choose a valid task!")
                if command1=='0':
                    break
                if command1=='1':
                    self.print_submenu()
                    command2=input("Choose an option: ")
                    while command2 not in commands2:
                        command2 = input("Choose a valid task!\n")
                    if command2=='a':
                        self._make_a_move()
                    if command2=='b':
                        self._change_pos()

            except ValueError as e:
                print(e)
            except KeyError as e:
                print(e)
            except Exception as e:
                print(e)
    def _make_a_move(self):
        move=input("How should I move?\n")
        move=move.split(" ")
        while move[0]!="move":
            move = input("Write a reasonable task!\n")
            move = move.split(" ")
        if len(move)==1:
            move.append(1)
        else:
            move[1]=int(move[1])
        self._service._move(move[1])



    def _change_pos(self):
        positions=["up","down","left","right"]
        pos=input("What way should I go?\n")
        while pos not in positions:
            pos = input("Never heard of this direction?\n")
        self._service._change_ways()



