v=list(map(int,input().split()))
h=list(map(int,input().split()))
v=sorted(v)
h=sorted(h)
print(v,h)
for i in range(0,len(v)):
    if v[i]>h[i]:
        print("Lose")
        break
else:
    print("Win")
