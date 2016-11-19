#coding=utf-8
import asyncore,socket
from time import ctime

class EchoHandler(asyncore.dispatcher_with_send):
    
    def handle_read(self):
        data = self.recv(8192)

        if data:
            self.send('%s  :  %s'%(ctime(),data))
            
class Server(asyncore.dispatcher):
    def __init__(self,addr):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(addr)
        self.listen(5)

    def handle_accept(self):
        conn,addr= self.accept()
        print "connect from",addr
        handler = EchoHandler(conn)

c = Server(('192.168.1.3',9999))
asyncore.loop()
        
