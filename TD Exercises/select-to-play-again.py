number = float(input("Nombre:"))
repeater = 1
while repeater > 0:
    print("Le carre de ce nombre est", number**2)
    print("Voulez-vous recommencer?")
    choice = str(input())
    if choice == "oui":
        repeater = repeater + 1
        number = float(input("Nombre:"))
    else:
        repeater = -1 
        print("Au revoir")