n=input()
count=0
for i in n:
  if (i.isalpha()!=True and i.isnumeric()!=True):
    count=count+1
print(count)