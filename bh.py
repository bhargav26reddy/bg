l,k=map(str,input().split())
count=0
for i in range(len(l)):
        if(l[i]!=k[i]):
            count+=1
if(count==1):
    print("yes")
else:
    print("no")
