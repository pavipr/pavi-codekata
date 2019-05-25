
  

n=int(input(""))
q=int(input(""))
if(n,q<=100000):
  for i in range(n,q+1):
    order=len(str(i))
    temp=i
    s=0
    while(temp>0):
      re=temp%10
      s+=re**3
      temp//=10
    if(i==s):
      print(i)




