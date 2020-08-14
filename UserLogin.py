
a="AnuAnala"
b='12345'
for i in range(0,4):
    login=input("Login-")
    password=input("Password-")
    if login == a or password == b:
        print("Login Successful")
        break
    else:
        print("Login Or Password Is Incorrect,Please Try Again")
else:
    print("Sorry Your Account Is Blocked")
            
    
