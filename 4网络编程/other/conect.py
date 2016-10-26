#coding=utf-8
from socket import *
import sys

HOST = sys.argv[1]                #IP
PORT = int(sys.argv[2])         #端口
BUFSIZE =1024                      #传输量
ADDR = (HOST,PORT)            #地址

sockfd = socket(AF_INET,SOCK_STREAM)    #创建套接字对象,网络传输,TCP模式

sockfd.connect(ADDR)                #连接地址
while True:                                    #等待键盘输入>发送>接受>打印>等待
    data = raw_input('>')               
    if not data:
        break
    sockfd.send(data)                   #用套接字发送信息到服务端
    data = sockfd.recv(BUFSIZE) #接受服务端发送来的信息并打印
    print data                                          

sockfd.close()