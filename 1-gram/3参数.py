#!/usr/bin/python

def fun(x,*args,**kwargs):
    print x
    print args
    print kwargs

fun(1,2,3,4,a = 5,b = 6)
