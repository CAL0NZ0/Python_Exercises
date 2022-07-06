# This code takes a number as input and outputs a list of all the different divisors of the number. 

num = int(input('Enter number: '))
divisor_list = []

for x in range(1,num+1):
    if num % x == 0:
        divisor_list.append(x)

for i in divisor_list:
    print(i)

