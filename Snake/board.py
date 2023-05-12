from texttable import Texttable


class GameError(Exception):
    pass


class Board:
    def __init__(self,file_name):
        self._dim=0
        self._file_name = file_name
        self._pos=""
        self._nr_apples=0
        self._read()
        self._data = [[" " for _ in range(self._dim)] for _ in range(self._dim)]

    def _read(self):

        with open(self._file_name, 'r') as f:
            line = f.readline()
            commands = line.split(",")
            self._dim = int(commands[0])
            self._nr_apples = int(commands[1])
            self._pos = commands[2]

        f.close()



    def _place(self, element, row: int, col: int):

        if element not in ['+','.','*']:
            raise GameError("Place a valid element!")
        if not (0<=col<self._dim) or not (0<=row<self._dim):
            raise GameError("Oops! It's outside of the board!")
        if self._data[row][col] != " ":
            raise GameError("First come, first served! Pick another spot.")
        if self._dim<3:
            raise GameError("Table must be at lest 5x5!")
        # if element=='.':
        #     if self._data[row+1][col]=='.' or self._data[row-1][col]=='.' or self._data[row][col+1]=='.' or self._data[row][col-1]=='.':
        #         raise GameError("Apple is adjacent to other apples!")

        self.set_data(element,row,col)


    def _get_rows(self, row):
        out=[]
        for el in row:
            out.append(el)
        return out

    def __str__(self):
        board = Texttable()
        for i in range(self._dim):
            board.add_row(self._get_rows(self._data[i]))
        return board.draw()

    @property
    def data(self):
        return self._data
    def data_place(self,row,col):
        return self._data[row][col]


    def set_data(self, element, row, col):
        self._data[row][col] = element
