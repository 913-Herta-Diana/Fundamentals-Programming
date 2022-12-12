class date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
days_m=[31,28,31,30,31,30,31,31,30,31,30]

def number_of_leap_years(x):
    an=x.year
    k=0
    if x.month<=2: #check if it's february, and we need to take leap years into consideration
        an-=1
    return (an//4)-(an//100)+(an//400)

def subtract_dates(date1,date2):
    s1=date1.year*365+date1.day

    for i in range(0,date1.month-1):
        s1+=days_m[i]
    s1+=number_of_leap_years(date1)

    s2=date2.year*365+date2.day
    for i in range(0,date2.month-1):
        s2+=days_m[i]
    s2+=number_of_leap_years(date2)

    return (s2-s1)

if __name__ == '__main__':
    date1=date(1,9,2014)
    date2=date(3,9,2020)
    print("The age in number of days:")
    subtract_dates(date1,date2)