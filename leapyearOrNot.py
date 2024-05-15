# question 18 - check whether a given number is leap year or not

def checkLeap(year):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        print("Given year is a leap year")
    else:
        print("Given year is not a leap year")
year = int(input("Enter year: "))
checkLeap(year)