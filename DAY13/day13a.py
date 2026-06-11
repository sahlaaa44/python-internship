users={}
email = input("enter email :")
password = input("enter password :")

if email in users:
    print("email is already exists")
else:
    users[email] = password
    print("registered successfully")

print(users)     
