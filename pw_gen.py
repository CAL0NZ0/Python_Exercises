# This program will generate a random password.

import string    
import random  

def pw_difficulty():
    return str(input('Easy, Medium or Hard: ')).lower()

def password_generator(x):
    if x == "easy":
        print(easy)
    elif x == "medium":
        print(medium)
    elif x == 'hard':
        print(hard)
        
print('Please, choose length and difficulty for you pasword below')

pw_len = int(input('How many characters will your password be? '))
spec_char_list = ('!','@','#','$','%','&')
spec_chars = ''.join((random.choice(spec_char_list)) for x in range(25))
easy = ''.join(random.sample(string.ascii_letters,k=pw_len))
medium = ''.join(random.sample(string.ascii_letters + string.digits,k=pw_len))
hard = ''.join(random.sample(string.ascii_letters + string.digits + spec_chars,k=pw_len))


password_generator(pw_difficulty())