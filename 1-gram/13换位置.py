#!/usr/bin/python

def fun(l,n):
        
    while n != 0:
        l.insert(0,l[-1])
        del l[-1]
        n -= 1



while True:
    l = [1,2,3,4,5,6,7,8,9]
    print l
    num = input("please input 1-9: ")
    if num < 1 or num > 9:
        print "input again!"
        continue
    fun(l,num)
    print l
