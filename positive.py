x=input('Input:list1')
x=x.split()
for i in x:
  if int(i)<0:
    x.remove(i)
print(x)