a=[2,5,3,1,6]
l=[0,1,2]
r=[4,3,4]
ps=[]
ps.append(a[0])
for i in range(0,len(l)):
    ps.append(ps[i-1]+a[i])
for i in range(0,len(l)):
    a=l[i]
    b=r[i]
    if l[i]==0:
        print(ps[r[i]])
    else:
        print(p[b]-ps[a-1])
