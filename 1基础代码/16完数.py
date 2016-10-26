#!/usr/bin/python



for i in range(1,1001):
    num = 0
    for j in range (1,i / 2 + 1):
        if i % j == 0:
            num += j

    if num == i:
        print "%d "%num,

print ""
