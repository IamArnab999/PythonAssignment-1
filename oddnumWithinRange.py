l_ran = int(input("Enter lower range: "))
u_ran = int(input("Enter upper range: "))

for i in range(l_ran, u_ran+1):
    if i % 2 != 0:
        print(i)