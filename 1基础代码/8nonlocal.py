#!/usr/bin/python3

def fun_out():
    a = 4

    def fun_in():
#        b = 5
        nonlocal a
        a += 1

    fun_in()
    print (a)
#    print (b)


fun_out()
