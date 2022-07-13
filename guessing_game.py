# This program generates a random number between 1 and 9. The user guesses the number until the guess is correct. The computer will notify you if you are too low/high and then output the amount of tries it took.

# Type 'exit' as a guess to stop the program.


import random

def get_num():
        return input('Guess a number 1-9: ')

def guessing_game():
        computer = random.randint(1,9)
        player = None
        count = 0
        
        while player != computer and player != 'exit':
                player = get_num()
                count += 1
                
                if player == 'exit':
                        break
                elif int(player) < computer:
                        print('You guessed too low!')
                elif int(player) > computer:
                        print('You guessed too high!')
                else:
                        print("You guessed it in", count, "tries!")




                        
guessing_game()