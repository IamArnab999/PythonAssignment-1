# question 20 - count prime factors of an integer

def prime_factor(num):
    temp = num
    i = 2
    while temp>1:
        if temp % i == 0:
            print(i,end=",")
            temp = int(temp/i)
        else:
            i = i + 1
num = int(input("Enter the integer: "))
prime_factor(num)