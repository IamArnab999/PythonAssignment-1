# question 4

num = int(input("Enter the number: "))
rev_num = 0
while num != 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10
print("The reversed: " + str(rev_num))
# OR
'''
num = int(input("Enter the number: "))
print(str(num)[::-1])'''