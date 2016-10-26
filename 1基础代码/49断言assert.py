#!/usr/bin/python

a = input()


try:
    assert a > 5
    if a > 5:
        print "a > 5"
    else:
        print "a < 5"
except AssertionError:
    print "NO NO NO!!!"
