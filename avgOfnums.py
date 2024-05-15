# question 1

num = int(input("Enter how many numbers: "))
total_sum = 0

for i in range(num):
    numbers = float(input("Enter numbers: "))
    total_sum += numbers

avg = total_sum / num
print("Average of", num, "numbers is: ", avg)