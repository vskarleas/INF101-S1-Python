print("Calcule de la moyenne")
chi = float(input("Donner note de chimie:"))
if 0 <= chi <= 20:
    phy = float(input("Donner note de physique:"))
    if 0 <= phy <= 20:
        mat = float(input("Donner note de mathematiques:"))
        if 0 <= mat <= 20:
            inf = float(input("Donner note de informatique:"))
            if 0 <= inf <= 20:
                 z = (chi + phy + mat + inf) / 4
                 print("Ta moyenne est:", z)
            else:
                print("note de informatique n'est pas acceptee")
        else:
            print("note de mathematiques n'est pas acceptee")
    else:
         print("note de physique n'est pas acceptee")
else :
    print("note de chimie n'est pas acceptee")

   
