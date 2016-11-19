#!/usr/bin/python

class Node(object):
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class Linklist(object):
    def __init__(self):
        self.head = None

    def initlist(self,data):
        self.head = Node(0)

        p = self.head

        for i in data:
            node = Node(i)
            p.next = node
            p = p.next

    def show(self):
        p = self.head.next

        while p != None:
            print p.val,
            p = p.next
        print ""
    
    def getlength(self):
        p = self.head
        length = 0
        
        while p.next != None:
            length += 1
            p = p.next

        return length

    def insert(self,index,val):
        if index < 0 or index > self.getlength():
            print "index is error"
            return

        p = self.head

        j = 0
        while p.next != None and j < index:
            p = p.next
            j += 1

        node = Node(val,p.next)
        p.next = node






