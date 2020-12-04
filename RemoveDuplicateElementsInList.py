l=[1,1,2,2,2,2,1,3,5,6,5,4,3,5,7,7,9,9,0]
new=[]
for i in l:
    if i not in new:
        new.append(i)
print(new)
