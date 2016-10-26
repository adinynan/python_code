#!/usr/bin/python

from socket import *
from time import ctime

HOST = '192.168.1.188'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockpd = socket(AF_INET,SOCK_DGRAM)

sockpd.bind(ADDR)

while True:
    print "waiting for message"

    data,addr = sockpd.recvfrom(BUFSIZE)

    print "client addr:",addr

    sockpd.sendto('[%s]:%s'%(ctime(),data),addr)

sockpd.close()
