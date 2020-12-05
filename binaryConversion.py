n=int(input())
l=[]
rem=n%2
while (rem==0) or (rem==1):
      rem=n%2
      l.append(rem)
      n=n//2
      if n==0 or n==1:
            l.append(n)
            break
print(l[::-1])      
