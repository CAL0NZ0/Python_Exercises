# This program will take a number as input and compare it against an ordered
#  list and output if the number is in the list.

import random

def num_chk(x,y):
    if x in y:
        print(x, 'is in the lsit')
    else:
        print(x,'is not in the list.')
    

lst = sorted(random.sample(range(1,101),25))
num = input('What number would you like to check? ')

num_chk(num,lst)