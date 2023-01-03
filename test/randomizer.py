from random import randint, choices
from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters

def randomNumber(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)


def randomStringLower(n):
    string = "".join(choices(ascii_lowercase, k = n))
    return string

def randomStringUpper(n):
    string = "".join(choices(ascii_uppercase, k = n))
    return string

def randomStringUpLow(n):
    string = "".join(choices(ascii_letters, k = n))
    return string



# change the number based on how many digits u want
print(randomNumber(10))
print(randomStringLower(10))
print(randomStringUpper(10))
print(randomStringUpLow(10))