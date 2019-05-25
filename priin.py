n=int(input(""))
q=int(input(""))
if(n,q<=100000):
  for num in range(n,q):
     if(num>1):
      for i in range(2,num):
        if(num%i)==0:
          break
      else:
          print(num)



      
