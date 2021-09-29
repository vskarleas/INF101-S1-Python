import random
x = random.randint(0, 100)
print(x)
k = 0
r = 100
y = int(input("Quelle nombre pense toi que le program a choise entre 0 et 100? "))
g = 1
while g > 0:
    if y == x:
        print("Gane")
        g = 0
    elif y > x:
        print("Trop grand")
        print("Quelle nombre pense toi que le program a choise entre",k,"et", y-1)
        z = y - 1
        r = z
        y = int(input())
        if y < x:
            z = y
        else:
            z = z
    else:
        print("Trop petit")
        print("Quelle nombre pense toi que le program a choise entre ",y+1," et", r)
        z = y+1
        k = z
        y = int(input())
        if y > x:
            z = z
        else:
            z = y