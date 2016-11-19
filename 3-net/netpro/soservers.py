#!/usr/bin/python
#forking

from SocketServer import *
from time import ctime

class Server(ForkingMixIn,TCPServer):
    pass
class Handler(StreamRequestHandler):
    def handler(self):
        addr = self.request.getpeername()
        print 'got connection from',addr
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            self.request.send(('[%s]:%s'%(ctime(),data)).encode())
server = Server(('192.168.1.188',6666),Handler)
server.serve_forever()
