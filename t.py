l,m,n=map(int,input().split())
a=[]
h=len(str(l))
if(l%2==0):
    q=l//2
    for i in range(h):
        a.append(q)
if(len(a)==h):
    print("YES")
else:
    print("NO")
