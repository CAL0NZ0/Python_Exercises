# This is 'Cows and Bulls'. The program will generate a random 4-digit number. The user will guess the number and the program will track if there is a correct guess in the correct place and show the amount of 'Cows' for any correct guess in the correct place and show the amount of 'Cows' for any correct guess and 'Bulls' for wrong guesses.


import random
import functions

computer = [int(x) for x in str(functions.rnd_num(1000,9999))]
player = None
count = 0

while player != computer and player != 'exit':
    player = [int(x) for x in str(functions.get_num('Enter a four digit number: '))]
    cows = 0
    bulls = 0
    
    count += 1
    
    
    if player == 'exit':
        break
    if player == computer:
        print('You got it in', count, 'tries!')
        break
    if player[0] == computer [0]:
        cows += 1
    else:
        bulls += 1
    if player[1] == computer [1]:
        cows += 1
    else:
        bulls += 1
    if player[2] == computer [2]:
        cows += 1
    else:
        bulls += 1
    if player[3] == computer [3]:
        cows += 1
    else:
        bulls += 1
    print(cows, 'Cows &', bulls, 'Bulls')
