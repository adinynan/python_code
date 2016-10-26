#!/usr/bin/python

def bubble(l):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j],l[j + 1] = l[j + 1],l[j]
    print(l)

def selection_sort(l):
    for i in range(len(l)):
        min = i
        for j in range(i + 1,len(l)):
            if l[min] > l[j]:
                min = j
        if i != min:
            l[i],l[min] = l[min],l[i]

    print(l)

def insertion_sort(l):
    for i in range(1,len(l)):
        s = l[i]
        j = i

        while j > 0 and l[j - 1] > s:
            l[j] = l[j - 1]
            j -= 1
        l[j] = s

    print(l)

def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] < key:
            low += 1
        array[high] = array[low]
    array[low] = key
    return low
def quick_sort(array,low,high):
    if low < high:
        key = sub_sort(array,low,high)

        quick_sort(array,low,key - 1)
        quick_sort(array,key + 1,high)

list = [2,9,4,6,3,8,1,5]
#bubble(list)
selection_sort(list)
#insertion_sort(list)
#quick_sort(list,0,len(list) - 1)
#print(list)
