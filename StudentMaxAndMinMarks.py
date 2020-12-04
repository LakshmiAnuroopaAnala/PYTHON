n=[]
m=[]
for i in range(0,5):
    n1=input("Student Name ")
    m1=input("Student Marks ")
    n.append(n1)
    m.append(m1)

mx=m.index(max(m))
print("Max -",n[mx],m[mx])

mn=m.index(min(m))
print("Min -",n[mn],m[mn])

