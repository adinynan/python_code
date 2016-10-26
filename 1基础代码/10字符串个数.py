#!/usr/bin/python

def char(ch,char):
    n = len(char)
    i = 0
    num = 0

    while i < n:
        if char[i] == ch:
            num += 1
        i += 1

    return num

num = char('o',"hello world")
print num
