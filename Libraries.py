# import random
import statistics
from random import choice,randint,shuffle
coins = choice(["heads", "tails"])

print(coins)

number=randint(1,10)
print(number)

card=["jack","queen","king"]
shuffle(card)

for val in card:
    print(val)

print(statistics.mean([100,90]))

import sys
# python     Libraries.py   Hasib     Rahman
# interpreter---index0-------index1----index2
# if len(sys.argv)<2:
#     sys.exit("Too few arguments")
# elif len(sys.argv)>2:
#     sys.exit("Too many arguments")

# print("Hello, my name is",sys.argv[1])

if len(sys.argv)<2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)