#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

j = 0
for i in fibonacci(10000):
    j += 1
    if len(str(i)) == 1000:
        print j
        break

