#!/usr/bin/python

from multiprocessing import *

def worker():
    '''worker function'''
    print worker
    return

if __name__ == '__name__':
    jobs = []
    for i in range(5):
        p = Process(target = worker)
        job.append(p)
        p.start()

