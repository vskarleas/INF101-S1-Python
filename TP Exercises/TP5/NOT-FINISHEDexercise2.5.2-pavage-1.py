from turtle import *
from math import *

def diametre(nb_cotes, cote):
    diametre = cote/(sin(pi/nb_cotes))
    return diametre

def colonne_polygone(nb_poly, cote):
    b = 0
    a = 1
    c = 4
    angle = 150
    up()
    nb_cotes = 3
    while b<nb_poly:
        while a < c:
            down()
            forward(cote)
            right(angle-30)
            a = a + 1
            nb_cotes=3
        up()
        longeur = diametre(nb_cotes, cote) + 5
        longeur = longeur * (-1)
        goto(0, longeur)
        longeur = longeur + longeur
        a = 1
        nb_cotes = nb_cotes + 1
        c = c + 1
        angle = angle-30
        b = b+1

nb_poly = 5
cote = 40
colonne_polygone(nb_poly, cote)