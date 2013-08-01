#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-30 15:22:59
# @Author  : azurefang (xidianft@gmail.com)

def triangle_num(num):
	return num*(num+1)/2

def factors_num(num):
	triangle=triangle_num(num)
	factor=[]
	for x in xrange(1,int(triangle**0.5+1)):
		if triangle%x==0:
			if x not in factor:
				factor.append(x)
			if triangle/x not in factor:
				factor.append(triangle/x)
	return factor

num=1
while(len(factors_num(num))<=500):
	num+=1

print triangle_num(num)

#牛人的程序
'''
from math import *
import time

def NombreDiviseurs(nombre):
  diviseurs = 0
  for i in range(1,int(sqrt(nombre))+1):
    if (nombre%i)==0:
      diviseurs+=2
  return diviseurs

def NombreDiviseursTriangle(n):
  if (n%2)==0 :
    return NombreDiviseurs(n//2)*NombreDiviseurs(n+1)
  return NombreDiviseurs(n)*NombreDiviseurs((n+1)//2)

ti=time.time()
n=1
nd=1
while nd<500:
  n+=1
  if ((n*(n+1))%12)==0:
    nd=NombreDiviseursTriangle(n)
         

print "Triangle", n, " => ", n*(n+1)//2, "  (", nd, "diviseurs )"
print "Time taken(secs):", time.time() - ti
'''