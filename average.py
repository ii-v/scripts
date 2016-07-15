#!/usr/bin/env python3
from die import die

def throws():
    l = []
    for i in range(10000):
        k = die(6)
        l.append(k)
    return average(l)

def average(l):
    avg = sum(l) / len(l)
    return(avg)

print(throws())
