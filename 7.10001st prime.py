#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-23 12:04:45
# @Author  : azurefang (xidianft@gmail.com)

import math

def is_prime(num):
	sq=int(math.sqrt(num))
	if num%2==0:
		return False
	for x in xrange(2,sq+1):
		if num%x==0:
			return False
	return True

x=1
t=0
while t<10001:
	if is_prime(x):
		t+=1
	x+=1

print x-1