#!/usr/bin/env python
# -*- coding: utf-8 -*-

full_list = [map(lambda x:x * 100, range(3)),map(lambda x:x * 50, range(5)),map(lambda x:x * 20, range(11)),map(lambda x:x * 10,range(21)),map(lambda x:x * 5, range(41)),map(lambda x:x * 2, range(101)),map(lambda x:x, range(201))]

c = len([ (a,b,c,d,e,f,g) for a in full_list[0] for b in full_list[1] for c in full_list[2] for d in full_list[3] for e in full_list[4] for f in full_list[5] for g in full_list[6] if (a+b+c+d+e+f+g) == 200 ])

print c
