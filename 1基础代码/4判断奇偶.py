#!/usr/bin/python

def fun(l):
    i = 0
    j = len(l) - 1
    
    while i < j:
        while l[i] % 2 != 0:
            i += 1
        while l[j] % 2 == 0:
            j -= 1
        if i < j:
            l[i],l[j] = l[j],l[i]

l = [1,2,3,2,5,8,1,9,7,6,4,3,5]
print "before:",l

fun(l)
print "after:",l
