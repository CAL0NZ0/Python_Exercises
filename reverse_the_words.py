# This program will take a string as input and print it out backwards.

def get_string():
    return input('Give me some words or a phrase: ')

def reverse_the_words():
    string = get_string()
    string_list = string.split()
    string_reverse_list = string_list[::-1]
    string_reverse = " ".join(string_reverse_list)
    print (string_reverse)

reverse_the_words()