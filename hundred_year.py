# This code takes your name and age as input and out puts a message telling you what year you will be 100 years old in

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
copies = int(input('Enter amount of copies: '))


current_year = 2022

hundred_year = (100 - age) + current_year

for i in range(copies):
    print(name + " you will turn 100 years old in the year " + str(hundred_year))


