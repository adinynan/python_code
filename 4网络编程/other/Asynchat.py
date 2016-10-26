#coding=utf-8
from asynchat import async_chat
from asyncore import loop
import socket

class EchoHandler(async_chat):

    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator('\n')
        self.data = []

    def collect_incoming_data(self, data):
        #self.data.append(data)
        self.send(data)
        
    def found_terminator(self):
        self.data = []

    def handle_close(self):
        async_chat.handle_close(self)
        
'''      
class Server(dispatcher):
    def __init__(self,addr):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(addr)
        self.listen(5)
'''      
class Server(async_chat):
    def __init__(self,addr):
        async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(addr)
        self.listen(5)

    def handle_accept(self):
        conn,addr= self.accept()
        print "connect from",addr
        handler = EchoHandler(self,conn)

c = Server(('192.168.1.3',9998))
loop()
