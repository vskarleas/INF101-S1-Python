def functioning():
    repeater = 1
    liste = []
    counting = 0
    somme = 0
    n = int(input("Donner un nombre: "))
    while repeater > 0:
        if n > 0:
            liste.append(n)
            counting = counting + 1
            somme = somme + n
            n = int(input("Donner un nombre: "))
            repeater = repeater + 1
        elif n == 0:
            repeater = -1
        else:
            n = int(input("Donner un nombre: "))
            repeater = repeater + 1
    if counting == 0:
        cad = "No positive numbers added to find the moyenne"
        return cad
    else:
        moyenne = somme /counting
        return moyenne


def inverse(liste):
    inversed = []
    selector = -1
    selectorABS = abs(selector)
    while selectorABS <= len(liste):
        inversed.append(liste[selector])
        selector = selector -1
        selectorABS = abs(selector)
    return inversed

liste = [1, 3, 9, 6, 4]
print(inverse(liste))
print(functioning())
