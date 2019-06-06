import math
n,m=map(int,input().split())
p=(n*m)/math.gcd(n,m)
print(int(p))
