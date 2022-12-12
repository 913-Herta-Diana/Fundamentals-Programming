# Solve the problem from the second set here
def det_date(y, d):
    days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]
    if y % 4 == 0:
        days[1] = 29  # if it's a leap year
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Dec"]
    for i in range(len(months)):
        lenght = int(days[i])
        if d > lenght:
            d -= lenght
        else:
            return y, months[i], d


if __name__ == '__main__':
    d = int(input("input number of days:"))
    y = int(input("input year:"))
    print("The date you are looking for is:")
    det_date(y, d)
    if d == 1:
        print(det_date(y, d), "st")
    elif d == 2:
        print(det_date(y, d), "nd")
    if d == 3:
        print(det_date(y, d), "rd")
    else:
        print(det_date(y, d), "th")
