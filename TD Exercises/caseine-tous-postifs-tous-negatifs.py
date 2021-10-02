
positive = 0
negative = 0
playing = 1
sommePositive = 0
sommeNegative = 0
a = float(input("Nombre ?"))
while playing > 0:
    while a != 0:
        if a > 0:
            positive = positive + 1
            sommePositive = sommePositive + a
            a = float(input("Nombre ?"))
        else:
            negative = negative + 1
            sommeNegative = sommeNegative + a
            a = float(input("Nombre ?"))
    playing = 0
if a == 0 and positive == 0 and negative == 0:
    print("Seulement 0")
elif negative > 0 and positive == 0:
    print("Tous -")
elif positive > 0 and negative == 0:
    print("Tous +")
elif positive > 0 and negative > 0:
    print("Ni tous +, ni tous -. ")
    if (sommePositive + sommeNegative) > 0:
        print("Somme +.")
    elif (sommePositive + sommeNegative) < 0:
        print("Somme -.")
    else:
        print("La somme 0")
else:
    print("Seulement 0")