n=list(input())
m=len(n)//2
if len(n)%2==0:
  n[m]="*"
  n[m-1]="*"
else:
  n[m]="*"
for i in n:
  print(i,end="")
