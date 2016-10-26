#!/usr/bin/python
#coding=utf-8

s = raw_input('>>')

str = "%s   "%s

i = len(s) - 1

f = open('dict.txt')
try:
    for line in f:
        if str in line and s[0] == line[0] and s[i] == line[i]:
           print line
    f.next()
except:
    pass


