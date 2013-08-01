#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-23 00:14:39
# @Author  : azurefang (xidianft@gmail.com)


a=range(1,21)
for x in range(20):
	for y in range(x):
		if a[x]%a[y]==0:
			a[x]/=a[y]
t=1
for x in range(20):
	t*=a[x]
print t