try :
    num=int(input("enter a number"))
except ValueError:    
    print("invalid")
else:
    print("success")
    print("number is",num)