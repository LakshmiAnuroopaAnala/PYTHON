arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
l=[]
for i in arr2:
    l.extend([i]*arr1.count(i))
c=set(arr1)-set(arr2)
c=list(c)
c.sort()
for i in c:
    l.extend([i]*arr1.count(i))
print(l)












