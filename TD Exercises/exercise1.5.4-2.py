txt = input("Character: ")
x = txt.isupper()
y = txt.islower()
if x == True:
    print("is majuscule")
elif y == True:
    print("is miniscule")
else:
    print("Both characters exist")
while (x == True) or (y == True):
    txt = input("Character: ")
    if x == True:
        print("is majuscule")
    elif y == True:
        print("is miniscule")
