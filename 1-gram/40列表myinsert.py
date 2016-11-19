#!/usr/bin/python

class MyFun():
    def __init__(self,l):
        self.l = l

    def MyInsert(self,n,value):

        num = len(self.l)
        self.l.append(0)
        i = 0
        while i < num - n:
            self.l[num - i] = self.l[num - i - 1]
            i += 1

        self.l[n] = value

    def show(self):
        print self.l


L = MyFun([1,2,3,4,5,6])

L.MyInsert(2,100)

L.show() 
