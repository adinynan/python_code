#!/usr/bin/python

class TestStaticMethod():
    def foo():
        print "calling static method foo()"

    foo = staticmethod(foo)


TestStaticMethod.foo()

A = TestStaticMethod()

A.foo()


class TestClassMethon():
    def foo(cls):
        print "calling class method foo()"
        print "class",cls.__name__
    foo = classmethod(foo)

TestClassMethon.foo()
B = TestClassMethon()
B.foo()
