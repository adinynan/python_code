#!/usr/bin/python3

class Magic(object):

    def __getattr__(self,name):
        print ("you use getaddr")
        print (name)

    def __setattr__(self,name,value):
        print ("you usr setattr")
        self.__dict__[name] = value


m = Magic()

print (dir(m))

m.x
m.x = 7

print (m.__dict__)
print (m.x)
