#!/usr/bin/python

import threading
from time import sleep,ctime

def wait_for_event(e):
    '''wait for...'''
    print('wait for')
    event_is_set = e.wait()
    print('event set1:%s'%event_is_set)

def wait_for_event_timeout(e,t):
    '''wait t ...'''
    while not e.isSet():
        print('wait for..')
        event_is_set = e.wair(t)
        print('event set2:%s'%event_is_set)
        if event_is_set:
            print('event')
        else:
            print('other')

e = threading.Event()
t1 = threading.Thread(name='block',target=wait_for_event,args=(e,))
t1.start()

t2 = threading.Thread(name='nonblock',target=wait_for_event_timeout,args=(e,3))
t2.start()

print('wait before')
sleep(4)
e.set()
print('wait after') 


