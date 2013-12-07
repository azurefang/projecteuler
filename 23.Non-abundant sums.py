#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isAbundant(num):
    divisors = [1]
    i = 2
    while i * i <= num:
        if num % i == 0:
            divisors.append(i)
            divisors.append(num/i)
        i += 1
    return sum(set(divisors)) > num
abundants = set(i for i in range(1,28124) if isAbundant(i))
def abundantsum(i):
    return any(i-a in abundants for a in abundants)
print sum(i for i in range(1,28124) if not abundantsum(i))
