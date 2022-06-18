# This program generates two random sized list containing random numbers. If then
#   generate.s a new list containing the common numbers in each list without any
#   duplicates


import random

lst_amount = random.randint(15,30)

a = random.sample(range(1,101),lst_amount)
b = random.sample(range(1,101),lst_amount)

common_list = []

for num in a:
    if num in b and num not in common_list:
            common_list.append(num)
        
for x in sorted(common_list):
    print(x)
    
