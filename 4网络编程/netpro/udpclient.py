#!/usr/bin/python

from socket import *
import sys

HOST = SYS.argv[1]
PORT = int(sys.args[2])
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockpd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break

    sockpd.sendto(data,ADDR)

    data,ADDR = sockpd.recvfrom(BUFSIZE)
    print data

sockpd.close()
