poly = {6:1, 2:3, 1:0, 5:2} #Key is the puissance and the value is the factor of the x
poly2 = {5:2, 4:3}
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
    newPoly = {}
    newPoly.update(poly.items())
    newPoly.update(poly2.items())
    return newPoly

def somme_polynomesTwo(poly, poly2):
    F1= dict(poly)
    F2 = dict(poly2)
    somme = F1+F2
    return somme

print(somme_polynomesTwo(poly, poly2))