
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

