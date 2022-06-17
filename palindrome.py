#this code takes a string as input and prints if the string is a palindrome

isWord = str(input('Enter Word: '))

word = isWord.lower()

if word[::1] == word[::-1]:
    print(isWord, "is a papalindrome.")
else:
    print(isWord, "is not a palindrome.")