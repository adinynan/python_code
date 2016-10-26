#!/usr/bin/python

a = input()

l = [ [1],[1,1] ]

for i in range(2,a):
    #print l
    l.append([1,1])
    for j in range(1,i):
        l[i].insert(j,(l[i-1][j-1]+l[i-1][j]))

for x in l:
    print x
