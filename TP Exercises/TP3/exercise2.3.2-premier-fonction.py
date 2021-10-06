from turtle import *


def carres():
    #trace un carre de taille 100
    i = 1 #compteur de nombre des cotes
    while i <= 4:
        forward(100)
        right(90)
        i = i + 1



carres()
up()
forward(130)
down()
carres()