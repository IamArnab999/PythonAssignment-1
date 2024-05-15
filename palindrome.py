# question 14 - Program to check if a number is palindrome or not

n = int(input("Enter the number: "))
if str(n) == str(n)[::-1]:
    print("The number is palindrome")
else:
    print("The number is not palindrome")