
from src.services.services import Service
from src.domain.domain import Expense

def run_all_tests(print_success = False):
  vars = globals()

  for name, var in vars.items():
    if name.startswith("test_") and callable(var):
        var()
        print_success=True

  if print_success:
    print("All tests passed.")
def test_add_expense():
    srvs = Service(False)
    expense = Expense(15, 345, "boots")

    srvs.addition(expense)

    try:
        srvs.addition(expense)
        assert False
    except:
        pass

run_all_tests()
