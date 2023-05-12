from repository import Repo
from service import Player
from ui import UI

if __name__=="__main__":
    repository=Repo("sentences.txt")
    service=Player(repository)
    ui=UI(repository,service)
    ui.start()