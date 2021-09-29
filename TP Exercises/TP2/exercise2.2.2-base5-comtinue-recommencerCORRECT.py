import random
recommencer = 1
qlm = 0
qlr = 0
mnl = 0
while recommencer > 0:
    x = random.randint(0, 100)
    print(x)
    k = 0
    r = 100
    y = int(input("Quelle nombre pense toi que le program a choise entre 0 et 100? (5 essais)"))
    g = 5
    while 0 < g <= 5:
        if y == x:
            print("Gane")
            g = 6
        elif y > x:
            print("Trop grand")
            print("Quelle nombre pense toi que le program a choise entre",k,"et", y-1,"(",g-1,"essais)")
            z = y - 1
            r = z
            y = int(input())
            g = g - 1
            if y < x:
                z = y
            else:
                z = z
        else:
            print("Trop petit")
            print("Quelle nombre pense toi que le program a choise entre ",y+1," et", r, "(",g-1,"essais)")
            z = y+1
            k = z
            y = int(input())
            g = g - 1
            if y > x:
                z = z
            else:
                z = y
    if g == 5:
        print("You runned out of times. 5 times is maximum")
        qlr = qlr + 1
        mnl = mnl + 1
    if g < 5:
        qlr = qlr + 1
        mnl = mnl + 1
    if g == 6:
        print("You found the correct number after")
        qlm = qlm + 1
        mnl = mnl + 1
    print("Voulez vous recommencer?")
    choice = str(input("oui/non :"))
    if choice == "oui":
        recommencer = recommencer + 1
    else:
        recommencer = 0
print("You played", mnl,"times in total. You won", qlm,"times and you lost", qlr,"times")
if qlm >= 1:
    essais = qlr/mnl
    print("En moyene tu as utilise", essais, "essais")