from turtle import *

def polygone(nb_cotes, cote):
    angle = (360/nb_cotes)
    a = 0
    while a < nb_cotes:
        down()
        forward(cote)
        right(angle)
        a = a + 1

nb_cotes = 5
cote = 100
polygone = polygone(nb_cotes, cote)