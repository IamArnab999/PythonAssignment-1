# question 16 - read a num n and 1+2+3...n=?

n = int(input("Enter the number: "))
li = []
for i in range(1, n+1):
    li.append(i)
print("The sum of numbers till n is: ", sum(li))