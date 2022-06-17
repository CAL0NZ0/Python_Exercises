# This code takes a number as input and generates a list twice as long with
#   random number between 1 and ten times the input. It prints the list then
#   prints a new list containing only the first and last elemnts of the array

import random

def lst_ends():
    get_num = int(input('Give me a number: '))

    lst = random.sample(range(1,get_num*10),get_num*2)

    print(lst)

    new_lst = []

    for x in lst:
        new_lst.append(lst[0])
        new_lst.append(lst[-1])
        break

    print(new_lst)

lst_ends()