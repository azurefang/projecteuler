#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-25 11:09:44
# @Author  : azurefang (xidianft@gmail.com)
import math

def is_prime(num):
	sq=int(math.sqrt(num))+1
	if num%2==0 and num!=2 or num==1:
		return False
	for x in xrange(2,sq):
		if num%x==0:
			return False
	return True

print sum(x for x in range(1,10) if is_prime(x))