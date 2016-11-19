#!/usr/bin/python

import b

reload(b)

#import b

import c as C


if __name__ == '__main__':
    a = 10
    print __name__

    print b.__name__

    print a
    print b.a
    print C.a
