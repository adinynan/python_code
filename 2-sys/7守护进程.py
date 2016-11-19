#!/usr/bin/python

import multiprocessing
import time
import sys
import subprocess

def daemon():
    p = multiprocessing.current_process()
    print('Starting:',p.name,p.pid)
    sys.stdout.flush()
    time.sleep(3)
    print('Exiting :',p.name,p.pid)
    sys.stdout.flush()
    while True:pass

def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:',p.name,p.pid)
    sys.stdout.flush()
    print('Exiting :',p.name,p.pid)
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(name = 'daemon',target = daemon)
    d.daemon = True

    n = multiprocessing.Process(name = 'non-daemon',target = non_daemon)
    n.daemon = False

    d.start()
    time.sleep(4)
    n.start()
