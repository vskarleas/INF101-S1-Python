def LireListeEntiers():
    klm = 1
    liste_1=[]
    n = int(input())
    liste_1.append(n)
    while klm > 0:
        if n >= 0:
            n = int(input())
            liste_1.append(n)
            klm = klm +1
        else:
            liste_1.pop()
            klm = -1
    return liste_1

def LireListeReelsBornes(bmin=0, bmax=100):
    liste_2=[]
    h = 1
    n = int(input())
    if n <= bmax and n >=bmin:
            liste_2.append(n)
    else:
        h = -1
    while h > 0:
        if n <= bmax and n >=bmin:
            n = int(input())
            liste_2.append(n)
            h = h + 1
        else:
            liste_2.pop()
            h = -1
    #With this one, it doesn't work liste_2.sort()
    return liste_2

def MMSListe(liste_3):
    minimum = min(liste_3)
    maximum = max(liste_3)
    somme = 0
    for i in range(len(liste_3)):
        somme = somme + liste_3[i]
    return minimum, maximum, somme





cab = LireListeReelsBornes(bmin=0, bmax=100)
print(cab)
