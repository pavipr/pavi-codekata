import math
n,m=map(int,input().split())
p=n*m
q=int(math.sqrt(p))
if((q*q==p) or (q*q==0)):
  print("yes")
else:
  print("no")