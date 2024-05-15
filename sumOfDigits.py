num = int(input("Enter a number: "))
digis =[]
while num > 0:
    a = num % 10
    digis.append(a)
    num //= 10
print("The sum of digits is:", sum(digis))