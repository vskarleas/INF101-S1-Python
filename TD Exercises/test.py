def pairs(longeur):
    liste_3=[]
    o = 0
    klm = 0
    while 0 < longeur:
        liste_3.append(klm+2)
        klm = klm +2
        o = o +1
    return liste_3

longeur=6
print(pairs(longeur))