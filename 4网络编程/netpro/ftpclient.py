#!/usr/bin/python

from socket import *
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfp = socket(AF_INET,SOCK_STREAM)

sockfp.connect(ADDR)

data = ('>')

sockfp.send(data)
data = sockfp.recv(BUFSIZE)

sockfp.close()
