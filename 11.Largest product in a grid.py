#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-25 11:36:13
# @Author  : azurefang (xidianft@gmail.com)

file_open=open('11.txt','r')

def prod(n): #returns product of members of list n
    return(reduce(lambda a,b:a*b,n))

s=file_open.read().split()
a=[]
b=[]
c=[]
d=[]
for x in xrange(0,20):
	for y in xrange(0,17):
		a.append(prod([int(s[20*x+y+t]) for t in range(0,4)]))
for x in xrange(0,17):
	for y in xrange(0,20):
		b.append(prod([int(s[20*(x+t)+y]) for t in range(0,4)]))
for x in xrange(0,17):
	for y in xrange(0,17):
		c.append(prod([int(s[20*(x+t)+y+t]) for t in range(0,4)]))
for x in xrange(0,17):
	for y in xrange(3,20):
		d.append(prod([int(s[20*(x+t)+y-t]) for t in range(0,4)]))
print max(max(a),max(b),max(c),max(d))