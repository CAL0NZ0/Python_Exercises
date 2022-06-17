# This code takes a number as input and determines wheter it's prime or not

def get_num(help_text):
    return int(input(help_text))

num = get_num('Give me a number: ')


for x in range(2,num):
    if num % x == 0:
        print(str(num) + ' is not a prime number.')
        break
    else:
        print(str(num) + ' is a prime number.')
        break