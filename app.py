def check_leap_year(year):
    if(year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
         print("a")
    else:
        print("b")


year = int(input())
check_leap_year(year)
