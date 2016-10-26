#!/usr/bin/python

__metaclass__ = type
class Person:

    def __init__(self):
        self.height = 164

    def about(self,name):
        print "{} is about {}".format(name,self.height)


class Girl(Person):
    def __init__(self):
        super(Girl,self).__init__()
        self.breast = 92

    def about(self,name):
        print "{} is a girl,she is about {},and her breast is {}".format(name,self.height,self.breast)
        super(Girl,self).about(name)


Chan = Girl()
Chan.about("DiaoChan")
