# This is the Guessing Game 2. In this edition, the user inputs a number between 1 and 25. The computer will guess the number until it get's it correct.

import random
from webbrowser import get

def get_num():
    return int(input('Enter a number between 1 and 25: '))


def guessing_game2():
    player = get_num()
    lst = list(range(1, 101))
    computer = None
    count = 0

    
    while computer != player:
        computer = int(random.choice(lst))
        count += 1

        if computer < player:            
            lst = list(range(computer + 1, computer + 10))

        elif computer > player:            
            lst = list(range(1, computer))
            
        else:
            if count == 1:
                print ('Computer guessed', player, 'in 1 try!')
            else:
                print('Computer guessed', player, 'in', count, 'tries!')
        
            
        

guessing_game2()