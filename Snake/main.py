from board import Board
from player import Player
from ui import UI

if __name__=="__main__":
    repo=Board("coordinates.txt")
    serv=Player()
    serv._place_snake()
    serv._place_apples()
    print(serv)
    ui=UI(serv)
    serv._move_snake_up()
    serv._move_snake_up()
    ui._start()
    print("\n",serv)
