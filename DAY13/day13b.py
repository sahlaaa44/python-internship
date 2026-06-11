users={
    "tasks@gmail.com":"213hyeiued"
}
email = input("enter email :")
password = input("enter password :")

if  email in users and users[email] == password:
    print("login successfully")
else:
    print("invalid")    