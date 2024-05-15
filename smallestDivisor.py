def smallest_divisor(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i

num = int(input("Enter a number: "))
divisor = smallest_divisor(num)
print("Smallest divisor of", num, "is:", divisor)