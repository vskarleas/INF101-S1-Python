password = 'abcdef'
i = str(input("Add your password to login: "))
kln = 0
if i != password :
    while kln < 4 :
        if i != password :
            print("Wrong password, try again!")
            i = str(input("Add your password to login: "))
            kln = kln + 1
        if i != password and kln == 4:
            print("You runned out of times")
        if i == password:
            kln = 5
    print("Access authorised!")
else :
    print("Access authorised!")