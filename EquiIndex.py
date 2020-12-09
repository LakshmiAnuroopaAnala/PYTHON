l=[-7,1,5,2,-4,3,0]
l2=[]
l2.append(l[0])
for i in range(1,6):
    ls=0;rs=0
    for j in range(0,i):
        ls+=l[j]
    for k in range(i+1,6):
        rs+=l[k]
    if ls==rs:
        print(i)
        break
