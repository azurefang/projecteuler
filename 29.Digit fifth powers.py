#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = []
for i in xrange(2, 999999):
    s = str(i)
    total = 0
    for j in s:
        total += int(j) ** 5
    if total == i:
        a.append(i)
print sum(a)

