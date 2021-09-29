import random
qlm = random.randint(1, 1000)
qlr = 1001
repeat = 10
while repeat == 10:
    while qlm != 1001:
        x = random.randint(0, 100)
        print(x)
        k = 0
        r = 100
        y = int(input("Quelle nombre pense toi que le program a choise entre 0 et 100? (5 essais)"))
        g = 5
        while 0 < g <= 5:
            if y == x:
                print("Gane")
                j = g -1
                g = 6
            elif y > x:
                print("Trop grand")
                print("Quelle nombre pense toi que le program a choise entre",k,"et", y-1,"(",g-1,"essais)")
                z = y - 1
                r = z
                print("Voulez-vous recommencer? (o/n)")
                choice = str(input())
                if choice == "n":
                    print("Ok, you can continue trying")
                else:
                    qlm = 1001
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
                print("Voulez-vous recommencer? (o/n)")
                choice = str(input())
                if choice == "n":
                    print("Ok, you can continue trying")
                else:
                    qlm = 1001
                y = int(input())
                g = g - 1
                if y > x:
                    z = z
                else:
                    z = y
        if g == 5:
            print("You runned out of times. 5 times is maximum")
        if g == 6:
            print("You found the correct number after", j,"times")
            print("Voulez-vous recommencer? (o/n)")
            choice = str(input())
            if choice == "n":
                print("Ok, you can continue trying")
            else:
                qlm = 1001

    while qlm == 1001:
        x = random.randint(0, 100)
        print(x)
        k = 0
        r = 100
        y = int(input("Quelle nombre pense toi que le program a choise entre 0 et 100? (5 essais)"))
        g = 5
        while 0 < g <= 5:
            if y == x:
                print("Gane")
                j = g -1
                g = 6
            elif y > x:
                print("Trop grand")
                print("Quelle nombre pense toi que le program a choise entre",k,"et", y-1,"(",g-1,"essais)")
                z = y - 1
                r = z
                print("Voulez-vous recommencer? (o/n)")
                choice = str(input())
                if choice == "n":
                    print("Ok, you can continue trying")
                else:
                    qlm = random.randint(1, 1000)
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
                print("Voulez-vous recommencer? (o/n)")
                choice = str(input())
                if choice == "n":
                    print("Ok, you can continue trying")
                else:
                    qlm = random.randint(1, 1000)
                y = int(input())
                g = g - 1
                if y > x:
                    z = z
                else:
                    z = y
        if g == 5:
            print("You runned out of times. 5 times is maximum")
        if g == 6:
            print("You found the correct number after", j,"times")
            print("Voulez-vous recommencer? (o/n)")
            choice = str(input())
            if choice == "n":
                print("Ok, you can continue trying")
            else:
                qlm = random.randint(1, 1000)