#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = []
for n in xrange(3, 1002, 2):
    a.append(2 * ((n * n)  + n - 1 + (n - 2) * (n - 2)))
print sum(a) + 1
