poly = {2:1, 4:3, 0:-3} #Key is the puissance and the value is the factor of the x
poly2 = {3:4, 4:8, 7:3}
from copy import *

def lire(n):
    poly = {}
    while n+1 > 0:
        print("Please give the coefficient for ", n)
        cof = int(input())
        poly.update({n: cof})
        n = n -1
    return poly

def evaluer(poly, x):
    sum = 0
    for k in poly:
        sum = sum + poly[k]*(x**k)
    return sum

def simplifier(poly): #Υπάρχει ένα θέμα εδώ. Θα το ξανακάνω με το αξαπητό μου deepcopy
    newdico = {}
    for key, value in poly.items():
        if value == 0:
            newdico.update({key: value})

    for newKey, newValue in newdico.items():
        poly.pop(newKey)
    return poly

def affiche(poly):
    liste = []
    finalListe = []
    simplified = simplifier(poly)
    for k, v in simplified.items():
        if k == 0:
            affiche = str(v)
        elif k == 1:
            affiche = str(v) +"x"
        else:
            affiche = str(v) +"x^" + str(k)
        liste.append(affiche)
    finalListe.append(liste[0])
    for l in range(1,len(liste)):
        if liste[l][0] == "-":
            finalListe.append(liste[l])
        else:
            demo = "+" + liste[l]
            finalListe.append(demo)
    print(*finalListe, sep="")

def afficheTwo(poly):
    for k in (poly.keys())[:-1]:
        print(poly[k], "*x^", k,"+", sep="", end="")
    k = len(poly.keys())(-1)
    print(poly[k], "*x^", k,"+", sep="", end="")

def somme_polynomes(poly, poly2):
    newPoly = deepcopy(poly)
    for coeff in poly2: #every key of poly2
        if coeff in newPoly:
            newPoly[coeff] = newPoly[coeff] + poly2[coeff]
        else:
            newPoly[coeff] = poly2[coeff]
    return newPoly

def produit_polynomes(poly, poly2):
    newPoly = {}
    for key, value in poly.items():
        for key2, value2 in poly2.items():
            newPoly[key2+key]=value2*value
    return newPoly

def derivee_polynome(poly):
    derivee = {}
    for key, value in poly.items():
        if key!=0:
            derivee[key-1]=key*value
    return derivee


print(produit_polynomes(poly, poly2))
print(poly)
print(simplifier(poly))
affiche(poly)
print(somme_polynomes(poly, poly2))