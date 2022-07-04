# This is Hangman. It references the file sowpods_list.txt.

from unicodedata import name
import requests
import random
from bs4 import BeautifulSoup

## Gets the list of words from a website and writes them to a .txt file.

# def sowpods_list():
#   get_site = requests.get('http://norvig.com/ngrams/sowpods.txt')
#   words = BeautifulSoup(get_site.content, 'html.parser')
#   sowpods = list(words)

#   with open('sowpods.txt', 'w') as file:
#     for x in sowpods:
#       file.write(x)

# sowpods_list()


## Chooses one random word from the list.
with open('sowpods.txt', 'r') as file:
  all_words = list(file)
  word = random.choice(all_words)
  word = word.replace('\n','')

if __name__ == '__main__':
  print("Welcome to hangman!!")
guesses = "_" * len(word)
word = list(word)
guesses = list(guesses)
guess_lst = []
letter = input("Guess a letter: ").upper()
tries = 0

while True:
  
  if letter in guess_lst:
    letter = ''
    print('You already guessed this letter. ')
  elif letter in word:
    letter_index = word.index(letter)
    guesses[letter_index] = letter
    word[letter_index] = '_'
  else:
    print(''.join(guesses))
    if letter != '':
      guess_lst.append(letter)
    letter = input("Guess a letter: ").upper()

  if '_' not in guesses:
    print (''.join(guesses))
    print('Boomshakalaka! You guessed the word!!')
    break