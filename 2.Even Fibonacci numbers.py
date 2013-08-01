#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-21 17:29:35
# @Author  : azurefang (xidianft@gmail.com)

sum = 0
formernum = 1
currentnum = 2
while currentnum <=4000000:
	if currentnum&1 == 0:
		sum += currentnum
	currentnum,formernum=currentnum+formernum,currentnum
print sum