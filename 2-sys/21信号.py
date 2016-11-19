#!/usr/bin/python
#coding=utf-8

from signal import *


alarm(3)

signal(SIGALRM,SIG_DFL)#д╛хожуж╧
signal(SIGALRM,SIG_IGN)#╨Жбт

while True:
    pass
