


n=int(input(""))
t=n
rev=0
while(n>0):
  di=n%10
  rev=rev*10+di
  n=n//10
if(t==rev):
  print("yes")
else:
  print("no")
