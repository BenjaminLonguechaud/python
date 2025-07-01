
""" random.py """
""" Random functions """

from random import random, randrange, randint
from random import choice, sample

__counter = 0

def printRandomNumbers():
    global __counter
    __counter += 1
    print(random())
    print(randrange(1), end=' ')
    print(randint(0, 1))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def printNumbersFromList():
    # Random element from the input sequence
    print(choice(my_list))
    # List with the choice
    print(sample(my_list, 5))