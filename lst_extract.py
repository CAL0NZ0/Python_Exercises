# Named "lessThan30" this code takes a number as input and compares that number to
#   a list. It then outputs a new list containing numbers less than the input
#   number

num = int(input("Enter number: "))
new_list = []

list = [1, 23, 34, 24, 64, 38, 18, 96, 50]

for i in list:
    if i < num:
        new_list.append(i)

print(new_list)
