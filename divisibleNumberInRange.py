l_ran = int(input("Enter lower range: "))
u_ran = int(input("Enter upper range: "))
givnum = int(input("Enter a number: "))

for i in range(l_ran, u_ran+1):
    if i % givnum == 0:
        print(i)