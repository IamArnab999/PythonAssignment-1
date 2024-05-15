# question 21 - check whether a number is armstrong number or not
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return number == armstrong_sum

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")