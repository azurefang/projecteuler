#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = set()
for i in xrange(2, 101):
    for j in xrange(2, 101):
        a.add(pow(i, j))

print len(a)
