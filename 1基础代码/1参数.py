#!/usr/bin/python
#coding=utf-8

# 定义位置参数的函数
def fun(a,b):
    print a,b

# 定义默认值参数

def fun1(a,b = 100):
    print a,b

# 定义收集位置实参的方式

def fun2(*a):
    print a

    
# 收集字典参数

def  fun4(**a):
    print a


fun(1,2)

fun1(1,2)

fun2(1,2,3,4,5)


fun4(a = 1,b = 2,c = 3)
