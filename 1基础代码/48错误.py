#!/usr/bin/python

def div(a,b):
    c = None
    try:
        c = a / b
    except ZeroDivisionError:
        print "Zero can not be division"
    except TypeError:
        print "please input the right num"
    else:
        print "else....."
    finally:
        print "finally...."

    return c

result = div(3,1)

print result

