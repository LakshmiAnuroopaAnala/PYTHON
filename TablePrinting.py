#PROGRAM TO PRINT A PARTICULAR TABLE U WANT
n=int(input("Enter A Value-"))
r1=int(input("Enter Range1-"))
r2=int(input("Enter Range2-"))
if r1<r2:
    for i in range(r1,r2+1):
        print(n,"*",i,"=",(n*i))
else:
    for i in range(r1,r2-1,-1):
         print(n,"*",i,"=",(n*i))