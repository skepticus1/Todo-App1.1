# random number with lower and upper bounds

import random

play = True
while play:
    low = int(input("please enter the lower number: "))
    high = int(input("please enter the higher number: "))
    print(random.randint(low, high))
    