poly = {6:1, 2:3, 5:2} #Key is the puissance and the value is the factor of the x
poly2 = {5:2}
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
    liste = []#We can do this and with deepcopy as well
    for key, value in poly.items():
        if value == 0:
            liste.append(key)
    for i in range(len(liste)):
        poly.pop(key)
    return poly

def affiche(poly):
    liste = []
    for k, v in poly.items():
        affiche = str()
        affiche = str(v) +"x^" + str(k)
        liste.append(affiche)
    print(*liste, sep="+")

def afficheTwo(poly):
    for k in (poly.keys())[:-1]:
        print(poly[k], "*x^", k,"+", sep="", end="")
    k = len(poly.keys())(-1)
    print(poly[k], "*x^", k,"+", sep="", end="")

def somme_polynomes(poly, poly2):
    newPoly = deepcopy(poly)
    for coeff in poly2:
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