# question 17 - print all prime numbers within a given range

l_rng = int(input("Enter the Lower range: "))
u_rng = int(input("Enter the upper range: "))

for num in range(l_rng, u_rng + 1):
    if num>1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)