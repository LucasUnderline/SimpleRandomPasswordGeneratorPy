import random
from time import sleep

password = ''
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&?-_'
numberOfStrings = int(input('How many Password?: '))
numberOfCharacters = int(input('How many characters in each password?: '))


for x in range(numberOfStrings):
    for c in range(numberOfCharacters):
        password += random.choice(characters)

    print(password)
    password = ''
    sleep(.3)