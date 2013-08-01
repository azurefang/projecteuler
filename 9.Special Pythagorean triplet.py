#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-25 10:49:43
# @Author  : azurefang (xidianft@gmail.com)

import math

for a in range(1,1000):
	for b in range(1,1000):
		if a+b+math.sqrt(a**2+b**2)==1000:
			print a*b*math.sqrt(a**2+b**2)
