#!/usr/bin/python

import signal
import time

signal.alarm(5)
signal.pause()#ÔÝÍ£

while True:
    time.sleep(1)
    print "wait....."
