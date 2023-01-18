from random import randint, choices, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters, punctuation
import pandas as pd

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

def randomNumberPunct(n):
    str1 = "".join(choices(punctuation, k = n))
    str1 += "". join(choices(digits, k=n))

    strList = list(str1)
    shuffle(strList)
    string = "".join(strList)
    return string

def randomNumberPunctLetters(n):
    str1 = "".join(choices(punctuation, k = n))
    str1 += "". join(choices(digits, k=n))
    str1 += "". join(choices(ascii_letters, k=n))

    strList = list(str1)
    shuffle(strList)
    string = "".join(strList)
    return string



# change the number based on how many digits u want
# print(randomNumber(10))
# print(randomStringLower(10))
# print(randomStringUpper(10))
# print(randomStringUpLow(10))
# print(randomNumberPunct(300))
# print(randomNumberPunctLetters(300))
x = randomNumber(1000000)
x = str(x)

file = open("1000000.txt", "w")
file.write(x)
file.close()