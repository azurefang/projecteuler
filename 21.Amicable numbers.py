#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

def getDivisors(num):
    mid = sqrt(num)
    divisors = [1]
    i = 2
    while i <= mid:
        if num % i == 0:
            divisors.append(i)
            divisors.append(num/i)
        i += 1
    return set(divisors)


amicable = []
for i in xrange(3, 10001):
    antiAmicable = sum(getDivisors(i))
    if i == sum(getDivisors(antiAmicable)) and i != antiAmicable:
        amicable.append(i)

print amicable
print sum(amicable)
