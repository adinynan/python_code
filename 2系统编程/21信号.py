#!/usr/bin/python
#coding=utf-8

from signal import *


alarm(3)

signal(SIGALRM,SIG_DFL)#Ĭ����ֹ
signal(SIGALRM,SIG_IGN)#����

while True:
    pass
