print("welcome to email slicer!")
email = input("enter the email address:")
if "@" in email:
    username = email.split("@")[0]
    domain = email.split("@")[1]
    print("username:",username)
    print("domain:", domain)
else:
    print("enterr a valid email address")