#!/usr/bin/python

from socket import *
import sys

sock = socket(AF_UNIX,SOCK_STREAM)
server_address = './test'

print >>sys.stderr,'connection to %
