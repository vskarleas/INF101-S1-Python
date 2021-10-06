from turtle import *
 
def carre(cote):
    #trace un carre de taille determinee:cote
    i = 1
    while i <= 4:
        forward(cote)
        right(90)
        i = i + 1

cote = int(input("Give a number: "))
carre(cote)
up()
forward(130)
down()
carre(cote)