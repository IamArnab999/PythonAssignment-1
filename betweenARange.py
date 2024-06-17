# question 15 - print all integers between 1 and 50 those are not divisible by 2/3

for i in range(1, 51):
    if i % 2 != 0 and i % 3 != 0:
        print(i)
