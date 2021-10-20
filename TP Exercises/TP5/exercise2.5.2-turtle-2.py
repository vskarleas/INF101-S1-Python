from turtle import *

def carre(cote_debut, nb_carres):
    reset()
    speed(1)
    shape('turtle')
    a = 1
    up()
    goto(-50,20)
    down()
    while a < 5:
        down()
        forward(cote_debut)
        right(90)
        a = a + 1
        up()
    b = 0
    while b < nb_carres-1:
        cote_debut = cote_debut*(2/3)
        a = 1
        while a < 5:
            down()
            forward(cote_debut)
            right(90)
            a = a + 1
            up()
        b = b + 1


cote_debut = 70
nb_carres = 5
carre(cote_debut, nb_carres)
