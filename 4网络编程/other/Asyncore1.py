#coding=utf-8
import asyncore, socket
class http_client(asyncore.dispatcher):
  def __init__(self, host, path):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.connect( (host, 80) )
    self.buffer = 'GET %s HTTP/1.0\r\n\r\n' % path
  def handle_connect(self):         #连接
    pass
  def handle_close(self):               #关闭
    self.close()
  def handle_read(self):                #读取
    print self.recv(8192)
  def writable(self):                       #判断是否可写
    return (len(self.buffer) > 0)
  def handle_write(self):               #写入
    sent = self.send(self.buffer)
    self.buffer = self.buffer[sent:]
c = http_client('www.baidu.com', '/')
asyncore.loop()