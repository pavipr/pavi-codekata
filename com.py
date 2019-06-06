n=int(input())
if n>0:
  for i in range (2,n//2):
    if(n%i)==0:
      print("yes")
      break
  else:
    print("no")
else:
  print("yes")

