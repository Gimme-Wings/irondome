year = int(input("what year is it? "))

if (year % 4 == 0) and (year % 100 == 0 and year %400 != 0):
    print("leap")
else:
    print("not a leap year")
