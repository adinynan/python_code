#!/usr/bin/python


class Test:
    def __enter__(self):
        print "enter...."

    def __exit__(self,type,value,traceback):
        print "exit...."
        print value

with Test() as Thing:    # Thing = Test()
    print "doing something"
