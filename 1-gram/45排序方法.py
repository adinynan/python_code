#!/usr/bin/python 

def mpao(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    print l

def xze(l):
    for i in range(len(l)):
        min = i
        for j in range(i+1,len(l)):
            if l[min] > l[j]:
                min = j
        if i != min:
            l[i],l[min] = l [min],l[i]
    print (l)

def chri(l):
    for i in range(1,len(l)):
        s = l[i]
        j = i

        while j > 0 and l[j-1] > s:
            l[j] = l[j-1]
            j -= 1
        l[j] = s
    print(l)

def k_su(l,i,j):
    key = l[i]
    while i < j:
        while i < j and l[j] >= key:
                j -= 1
        l[i] = l[j]
        while i < j and l[i] < key:
            i += 1
        l[j] = l[i]
    l[i] = key
    return i


def kuai_su(l,i,j):
    if i < j:
        key = k_su(l,i,j)

        kuai_su(l,i,key - 1)
        kuai_su(l,key + 1,j)


l = [5,8,9,4,3,6,1,7]
#mpao(l)
#xze(l)
#chri(l)
kuai_su(l,0,len(l)-1)
print l
