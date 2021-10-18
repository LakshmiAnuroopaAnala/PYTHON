a1=[9,45,67,78,90]
a2=[11,34,69,70,120,145]
result=[]
# Union Of Two Lists In Ascending Order
a1p=0 #pointer to a1
a2p=0  #pointer to a2
while(a1p<len(a1) and a2p<len(a2)):
    if a1[a1p]<a2[a2p]:
        result.append(a1[a1p])
        a1p+=1
    else:
        result.append(a2[a2p])
        a2p+=1
    #print(result)
    
while(a1p<len(a1)):
    result.append(a1[a1p])
    a1p+=1
    
while(a2p<len(a2)):
    result.append(a2[a2p])
    a2p+=1

print(a1,a2,result)
