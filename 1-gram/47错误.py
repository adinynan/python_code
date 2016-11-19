#!/usr/bin/python

def div(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print "Zero can not be division"
        print dir(e)
        print e.args
    except TypeError:
        print "please input the right num"

result = div(3,0)

print result

