n=int(input("enter"))
q=int(input("enter"))
if(n,q<=100000):
  for num in range(n,q+1):
     if(num>1):
      for i in range(2,num):
        if(num%i)==0:
          break
      else:
          print(num)



      