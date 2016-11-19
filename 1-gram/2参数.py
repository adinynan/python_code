#!/usr/bin/python3


# 收集部分位置参数，其他参数需按照关键字传递


def fun(*a,name):
    print (a)
    print (name)

fun(1,2,3,4,name = 10)

def fun1(name,*,a,b,c):
    print (name,a,b,c)


fun1('he',a = 1,b = 2,c = 3)
