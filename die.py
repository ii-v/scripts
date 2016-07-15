#!/usr/bin/env python3
# A simple die simulator/generator

from random import randrange

def die(sides):
    return(randrange(1, sides+1))

if __name__ == "__main__":
    for dice in range(5):
        print(die(6)) # this should print 5 random numbers between 1 and 6
