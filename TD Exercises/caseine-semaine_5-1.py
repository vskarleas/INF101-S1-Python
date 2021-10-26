def liste_decroissante(n):
    liste=[]
    while n+1 > 0:
        liste.append(n)
        n = n - 1
    return liste

def multiples(m, longeur):
    liste_2=[]
    h = 0
    while h < longeur:
        liste_2.append(m*h)
        h = h +1
    return liste_2

def pairs(longeur):
    liste_3=[]
    h = 0
    klm = 0
    while h < longeur:
        liste_3.append(klm)
        klm=klm+2
        h = h +1
    return liste_3

m=5
longeur=10
n = 6
print(liste_decroissante(n))
print(multiples(m, longeur))
print(pairs(longeur))