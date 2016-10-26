#!/usr/bin/python


def fib(max):
    a,b = 0,1
    while a < max:
        yield a
        a,b = b,a + b

for i in fib(100):
    print i
