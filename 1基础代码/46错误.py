#!/usr/bin/python3

def div(a,b):
    try:
        return a / b
#    except ZeroDivisionError:
    except (NameError,ZeroDivisionError):
#        print "NameError"
#    except:
        print ("Zero can not be divsion")
        return -1

result = div(3,0)

print (result)

print ("test over")
