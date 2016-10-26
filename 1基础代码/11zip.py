#!/usr/bin/python

keys = ['spam','eggs','toast']
vals = [1,3,5]

d = {}

for (k,v) in zip(keys,vals):
    d[k] = v

print d

