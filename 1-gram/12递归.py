#!/usr/bin/python 

def P(n,x):
    if n == 0:
        return 1
    elif n == 1:
        return x

    return ((2 * n - 1)*x*P(n - 1,x) - (n - 1)*P(n - 2,x)) / n

print P(4,6)

