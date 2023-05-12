import random

from texttable import Texttable

from board import Board


class Player(Board):
    def __init__(self):
        super().__init__("coordinates.txt")
        self._len_snake=3


    def __str__(self):
        board = Texttable()
        for i in range(self._dim):
            board.add_row(self._get_rows(self._data[i]))
        return board.draw()

    def get_coord(self,element):
        for i in range(self._dim):
            for j in range(self._dim):
                if self._data[i][j]==element:
                    return (i,j)

    def _place_apples(self):

        index=self._nr_apples
        while index>0:
            mov = False
            row = random.randint(0, self._dim - 1)
            col = random.randint(0, self._dim - 1)
            print(row,col)
            if self.data[row][col]==" ":
                if (row,col)==(0,0):
                    if self._data[row + 1][col] != '.' and self._data[row][col + 1] != '.':
                        mov=True
                elif (row,col)==(0,self._dim-1):
                    if self._data[row+1][col]!="." and self._data[row][col-1]!='.':
                        mov=True
                elif (row,col)==(self._dim-1,0):
                    if self._data[row][col+1]!='.' and self._data[row-1][col]!=".":
                        mov=True
                elif (row,col)==(self._dim-1,self._dim-1):
                    if self._data[row-1][col]!="." and self._data[row][col-1]!='.':
                        mov=True
                elif row==0:
                    if self._data[row + 1][col] != '.'  and self._data[row][col + 1] != '.' and self._data[row][col - 1] != '.':
                        mov = True
                elif col==0:
                    if self._data[row + 1][col] != '.' and self._data[row - 1][col] != '.' and self._data[row][col + 1] != '.':
                        mov = True
                elif row==self._dim-1:
                    if self._data[row-1][col] != '.'  and self._data[row][col + 1] != '.' and self._data[row][col - 1] != '.':
                        mov = True
                elif col==self._dim-1:
                    if self._data[row + 1][col] != '.' and self._data[row - 1][col] != '.' and self._data[row][col - 1] != '.':
                        mov = True
                else:
                    if self._data[row + 1][col] != '.' and self._data[row][col + 1] != '.' and self._data[row][col - 1] != '.' and self._data[row-1][col]!=".":
                        mov=True
            if mov==True:
                index-=1
                self._place('.', row, col)

    def _place_snake(self):

        middle=self._dim//2
        pos=self._pos

        if pos=="up":
            self._place('*', middle - 1, middle)
            for i in range(2):
                self._place("+", middle + i, middle)
        if pos=="down":
            for i in range(2):
                self._place("+", middle - i, middle)
            self._place('*', middle + 1, middle)
        if pos=="right":
            self._place('*',middle,middle+1)
            for i in range(2):
                self._place('+',middle,middle-i)
        if pos=="left":
            self._place('*',middle,middle-1)
            for i in range(2):
                self._place('+',middle,middle+i)

    def _find_pos(self):
        pos=""
        for i in range(self._dim):
            for j in range(self._dim):
                if self._data[i][j]=="*":
                    if self._data[i][j-1]=="+":
                        pos='right'
                    elif self._data[i][j+1]=="+":
                        pos="left"
                    elif self._data[i-1][j]=="+":
                        pos="down"
                    elif self._data[i+1][j]=="+":
                        pos="up"
        return pos

    def _move_snake_up(self):
        (row,col)=self.get_coord("*")
        empty=0

        if row==0:
            message="Game over!"
            return message
        else:
            self.set_data("*",row-1,col)
            for i in range(2):
                self.set_data("+",row+i,col)
                empty=i
            self.set_data(" ",row+empty+1,col)



    def _move_snake_down(self):
        pass
    def _move_snake_left(self):
        pass
    def _move_snake_right(self):
        pass
    def _check_game_over(self):
        pass

    def _move(self,steps):
        len=self._len_snake
        pos=self._find_pos()
        for i in range(steps):
            for j in range(len):
                if pos=="up":
                    for i in range(3):
                        self._move_snake_up()








"""
TODO
-moving the snake according to the positions function
-check if the snake hits his head function
-changing the position function (check if it's equal to already existent position)
-Exception: up,down-> left,right; left,right->down,up

-apple eating

"""

"""
HOTEL MANAGEMENT or another repository
File operations in Chaos and Order
"""

                



