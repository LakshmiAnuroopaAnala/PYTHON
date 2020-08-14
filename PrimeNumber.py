import math
n=int(input("Enter A Value - "))
sq=int(math.sqrt(n))
for i in range(2,sq+1):
    if n%i == 0:
        print(n,"Is A Composite number")
        break
else:
    print(n,"Is A Prime")
