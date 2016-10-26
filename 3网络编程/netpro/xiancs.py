#!/usr/bin/python

import socket,os,sys,traceback
from threading import *

host = '192.168.1.188'
port = 6666

def handler(clientsock):
    print 'new child'
    print 'got connection from',clientsock.getpeername()
    while True:
        data = clientsock.recv(1024)
        if not len(data):
            break
        clientsock.send('receive your message'.encode())

        clientsock.close()

s = socket.socket()
s.bind((host,port))
s.listen(5)

while True:
    try:
        clientsock,clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    t = Thread(target=handler,args=(clientsock,))
    t.setDaemon(1)
    t.start()
s.close()
