# This code takes two numbers as input and check if the second number can be
#  divided into the first

num = int(input('First number: '))
check = int(input('Second number: '))

if num % check == 0:
    print('Is divisible')

else: print('Is not divisible')