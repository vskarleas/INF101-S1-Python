from turtle import *
 
def carre(cote, x, y):
    #trace un carre de taille determinee:cote
    i = 1
    up()
    goto(x,y)
    while i <= 4:
        down()
        forward(cote)
        right(90)
        i = i + 1
        up()

x = int(input("Give x coordonees: "))
y = int(input("Give y coordonees: "))
cote = int(input("Give a number: "))
carre(cote, x, y)