from repository import TextFileRepo
from service import Service
from ui import UI

if __name__ == '__main__':
    text_file_repo = TextFileRepo()
    service = Service(text_file_repo)
    console = UI(service)
    console.start_menu()


