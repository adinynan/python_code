#!/usr/bin/python

class TestIter:
    def __init__(self,a):
        self.a = a

    def __iter__(self):
        return self

    def __next__(self):

        self.a += 1
        return self.a ** 2

a  = TestIter(2)


#print (a.__next__())
#print (a.__next__())

print a.__next__()

it = a.__iter__()

print it.__next__()
