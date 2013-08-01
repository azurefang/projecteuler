#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-22 23:08:15
# @Author  : azurefang (xidianft@gmail.com)


def is_palindrome(num):
	length=len(str(num))
	for x in xrange(0,length):
		if str(num)[x]!=str(num)[length-x-1]:
			break
	else:
		return True

print max([x*y for x in range(100,999) for y in range(100,999) if is_palindrome(x*y)])