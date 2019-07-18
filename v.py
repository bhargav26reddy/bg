c=input()
l=''
for i in range(0,len(c)-1,2):
  if(int(c[i+1])%2==0):
    l+=c[i]*int(c[i+1])
  else:
    l+=c[i]+c[i+1]
print(l)
