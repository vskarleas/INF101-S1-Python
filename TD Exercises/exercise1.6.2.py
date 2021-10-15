i = 1
entier = int(input("Donner un entier: "))
liste_pair = []
liste_impair = []
while i > 0:
    if entier == 0:
        i = 0
    if entier >0:
        if entier % 2 == 1:
            liste_impair.append(entier)
        else:
            liste_pair.append(entier)
        entier = int(input("Donner un entier: "))
        i= i + 1
    if entier < 0:
        entier = int(input("Donner un entier: "))
        i = i + 1
print("pairs:", liste_pair ,", impairs: ", liste_impair )
