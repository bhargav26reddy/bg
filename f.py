l,k=map(str,input().split())
for i in range(len(l)):
    if(l.count(l[i])==k.count(k[i])):
        print("yes")
        break
    else:
        print("no")
        break
