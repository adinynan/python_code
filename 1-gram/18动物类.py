#!/usr/bin/python
#coding=utf-8

class Animal(object):

    def __init__(self):
        print "A new animal"

    def call(self,yell):
        self.yell = yell


class Dog(Animal):

    def __init__(self):
        print "A dog"

    color = "yellow"

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

class Cat(Animal):
    color = "white"

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name
    

wang = Dog()
miao = Cat()

wang.setName("大黄")

print wang.getName()

wang.call("wangwang")
print wang.yell
miao.call("miaomiao")
print miao.yell

