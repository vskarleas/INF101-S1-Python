import random
x = random.randint(0, 100)
print(x)
k = 0
r = 100
y = int(input("Quelle nombre pense toi que le program a choise entre 0 et 100? "))
g = 1
while g < 5:
    if y == x:
        print("Gane")
        j = g -1
        g = 6
    elif y > x:
        print("Trop grand")
        print("Quelle nombre pense toi que le program a choise entre",k,"et", y-1)
        z = y - 1
        r = z
        y = int(input())
        g = g + 1
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
        g = g + 1
        if y > x:
            z = z
        else:
            z = y
if g == 5:
    print("You runned out of times. 5 times is maximum")
if g == 6:
    print("You found the correct number after", j,"times")