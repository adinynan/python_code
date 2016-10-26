#!/usr/bin/python

def fun(s):

    i = 0
    eg = '01234556789'
    l = []

    while i < len(s):
        if i == 0 and s[i] in eg:
            b = i
        if i > 0 and (s[i] in eg) and (s[i - 1] not in eg):
            b = i

        if i == len(s) - 1 and s[i] in eg:
            e = i
            l.append(int(s[b:e + 1]))
        if (i < len(s) - 1) and (s[i] in eg) and (s[i + 1] not in eg):
            e = i
            l.append(int(s[b:e + 1]))
            
        i += 1

    return l

s = raw_input()
print s
l = fun(s)
print l
