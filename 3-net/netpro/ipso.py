#!/usr/bin/python

import socket

packed = socket.inet_aton('192.168.1.188')

print 'Packed:',packed
print 'Unpacked:',socket.inet_ntoa(packed)

port = socket.htons(8888)
print 'port:',port
print 'unport:',socket.ntohs(port)
