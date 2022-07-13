#this is a classic Rock, Paper, Scissors game. the code takes two inputs
# and compares the inputs to choices to declare a winner

import random

choices = ('rock', 'paper', 'scissors')

p_one = str(input('Player one choice: ').lower())
p_two = random.choice(choices)



def rockPaperScissors(p_one,p_two):
    
    while (p_one in choices and p_two in choices):
        if p_one == p_two:
            print('Draw')
            break
        elif p_one == choices[0] and p_two == choices[1]:
            print('Player Two Wins!')
            break
        elif p_one == choices[0] and p_two == choices[2]:
            print('Player One Wins!')
            break
        elif p_one == choices[1] and p_two == choices[0]:
            print('Player One Wins!')
            break
        elif p_one == choices[1] and p_two == choices[2]:
            print('Player Two Wins!')
            break
        elif p_one == choices[2] and p_two == choices[0]:
            print('Player Two Wins!')
            break
        elif p_one == choices[2] and p_two == choices[1]:
            print('Player One Wins!')
            break
    else: print('Invalid choices')

rockPaperScissors(p_one,p_two)




        
