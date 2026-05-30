try :
    num=int(input("enter a number"))
    print(num)
except ValueError:
    print("wrong")
finally:
    print("finished")