# This is 'Cows and Bulls'. The program will generate a random 4-digit number.
#   The user will guess the number and the program will track if there is a
#   correct guess in the correct place and show the amount of 'Cows' for any 
#   correct guess and 'Bulls' for wrong guesses.


import functions

computer = str(functions.rnd_num(1000,9999))
player = None
count = 0

while player != computer and player != 'exit':
    player = functions.get_num('Enter a four digit number: ')
    cows = 0
    bulls = 0
    
    count += 1
    
    if player == 'exit':
        break
    elif player == computer:
        print('You got it in',count,'tries!')
        break
    for x in range(len(computer)):
        if player[x] == computer[x]:
            cows +=1
        else:
            bulls += 1
    print(cows,'Cows &',bulls,'Bulls')