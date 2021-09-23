password = 'abcdef'
i = str(input("Add your password to login: "))
while i != password :
    print("Wrong password, try again!")
    i = str(input("Add your password to login: "))
print("Access authorised!")
