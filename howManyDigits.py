# question 13 - Program to count the no. of digits in a numbers

n = int(input("Enter the number: "))
dig = []
while n>0:
    a = n % 10
    dig.append(a)
    n //= 10
print("The number of digits: ", len(dig))