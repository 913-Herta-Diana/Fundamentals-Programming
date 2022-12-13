from src.ui.ui import UserInterface
from src.ui.ui import print_menu
from src.services.test import test_add_expense
def main():
  ui = UserInterface()
  while True:
    print_menu()
    ui.handling_input()

if __name__ == "__main__":
    print(test_add_expense())
    main()
#