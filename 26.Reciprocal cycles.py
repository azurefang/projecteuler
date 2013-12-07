#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import count
def recLen(n):
    r = 10
    seen = {}
    for i in count(0):
        if r == 0:
            return 0
        elif r in seen:
            return i - seen[r]
        seen[r] = i
        r = 10 * (r % n)

maxLen, i = max((recLen(i), i) for i in range(2, 1000))
print i
