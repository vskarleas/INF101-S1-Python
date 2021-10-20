from turtle import *

def carre(cote):
    reset()
    speed(1)
    shape('turtle')
    a = 1
    up()
    goto(-50,20)
    down()
    while a < 5:
        down()
        forward(cote)
        right(90)
        a = a + 1

cote = 70
carre(cote)
