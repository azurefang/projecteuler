#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-30 16:49:33
# @Author  : azurefang (xidianft@gmail.com)

def triangle_num(num):
	return num*(num+1)/2

def factors_num(num):
	triangle=triangle_num(num)
	factor=0
	for x in xrange(1,int(triangle**0.5+1)):
		if triangle%x==0:
			factor+=2
	return factor

num=1
nd=1
while(nd<=500):
	num+=1
	if (num*(num+1)%12==0):
		nd=factors_num(num)

print triangle_num(num)