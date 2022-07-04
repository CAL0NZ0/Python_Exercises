# This code takes a number as input and prints if the number is even or odd.

x = int(input("Type in a number: "))

if x % 4 == 0 and x % 2 == 0:
    print(str(x) + " is an even number and multiple of 4.")
elif x % 2 == 0:
    print(str(x) + " is an even number.")
else:
    print(str(x) + " is an odd number.")