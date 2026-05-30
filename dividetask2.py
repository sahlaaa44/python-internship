def divide(a,b):
    if b==0:
# result=(10,45)
# print(result)
        raise ZeroDivisionError("cannot divide zero")
    return a/b
print(divide(10,10))

