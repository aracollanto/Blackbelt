# Ara E. Collanto
# Task 2

import random

x = random.randint(1,10)

while True:
    print ("Please enter a number from 1 to 10:", end=" ")
    y = int(input());
    if x==y:
        print ("Correct!")
        break
    elif x!=y:
        print ("Wrong, try again!")
    
