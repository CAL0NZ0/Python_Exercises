# This code takes a number as input and generates that many numbers in the 
#   Fibonacci sequence.

def get_num():
    return int(input('Give me a number: '))

def add_fib_sum():
    fib_sum = fib[-1] + fib[-2]
    fib.append(fib_sum)
    return fib

def fib_seq():
    count = 0
    while count <= seq_amount-1:
        add_fib_sum()        
        count += 1
    return fib[:seq_amount]



seq_amount = get_num()
fib = [1,1]

print(fib_seq())  