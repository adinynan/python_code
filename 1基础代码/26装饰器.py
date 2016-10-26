#!/usr/bin/python
#coding=utf-8

class Protest:
    def __init__(self):
        self.job = 'teacher'
        self.__name = 'cainiao'
    
    @property
    def name(self):
        return self.__name

    def __python(self):
        print "人生苦短，我用python"

    def code(self):
        print "which language do you like ?"
        self.__python()


p = Protest()
print p.job
#print p.__name

print p.name()

#p.__python()

p.code()
