s1,s2=0,1
for i in range(10):
  if i<=1:
    print(i)
  else:
    s=s1+s2
    print(s)
    s1=s2
    s2=s 