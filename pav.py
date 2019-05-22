try:
  a=float(input("enter"))
except ValueError:
  print("invalid")
if(a/2==0):
  print("even")
else:
  print("odd")