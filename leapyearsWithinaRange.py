# question 19 - print the list of leap years within a given range

l_rng = int(input("Enter the Lower range: "))
u_rng = int(input("Enter the upper range: "))

for year in range(l_rng, u_rng+1):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        print(year)