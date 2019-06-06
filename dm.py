n,p,m=input().split()
n=int(n)
m=int(m)
if p=='%':
  print(int(n%m))
else:
  print(int(n/m))