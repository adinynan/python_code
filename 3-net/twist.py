#!/usr/bin/python

from twisted.internet import protocol,reactor
from time import ctime

HOST = 'localhost'
PORT = 8888

class TSClntProtocol(protocol.Protocol):
	def sendData(self):
		data = raw_input('>>>')
		if data:
			print '..sending %s...'%data
			self.transport.write(data)
		else:
			self.transport.loseConnection()

	def connectionMade(self):
		self.sendData()
	
	def dataReceived(self,data):
		print data
		self.sendData()

class TSClntFactory(protocol.ClientFactory):
	protocol = TSClntProtocol
	clientConnectionLost = clientConnectionFailed = lambda self,connector,reason:reactor.stop()

reactor.connectTCP(HOST,PORT,TSClntFactory())
reactor.run()
