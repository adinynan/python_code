#coding=utf-8
from SocketServer import *
from time import ctime

class Server(ForkingMixIn,TCPServer):       #继承进程,TCP
    pass

class Handler(StreamRequestHandler):        #继承读,写类
    def handle(self):                                               #行为函数
        addr = self.request.getpeername()           #连接用户地址
        print 'got connection from',addr
        while True:                                                     
            data = self.request.recv(1024)              #接受信息
            if not data:
                break
            self.request.send('[%s] :%s'%(ctime(),data)) #发送信息
            
server = Server(('192.168.1.23',9999),Handler)   #实例化Server传入地址,读写类
server.serve_forever()      #运行服务器