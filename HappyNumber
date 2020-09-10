def Happy(num):
    square=0
    while num!=0:
        rem=num%10
        square=square+(rem**2)
        num=num//10
    if square>=0 and square<=9:
        if square==1 or square==7:
            print("Happy Number")
        else:
            print("Not A Happy Number")
    else:
        Happy(square)
number=int(input())
Happy(number)
