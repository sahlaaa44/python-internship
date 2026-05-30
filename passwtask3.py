class weakpassworderror(Exception):
    pass
def check(password):
    if len(password)<8:
        raise weakpassworderror("password must contain 8 characters")
    elif not any(char.isdigit() for char in password):
        raise weakpassworderror("password must contain digits")
    elif not any(char.isupper()for char in password):
        raise weakpassworderror("password must contain uppercase")
    else:
        print("right password")
try:
    password=input("enter password :")
    check(password)
except weakpassworderror as e:
    print("error:",e)
    


