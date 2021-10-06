from turtle import *
def rosace(x, y, nb, r):
    up()
    goto(x, y)
    for kappa in range (0, nb):
        down()
        circle(r)
        right(360/nb)


x = int(input("Donner x:"))
y = int(input("Donner y:"))
nb = int(input("Donner nombre des rosaces:"))
r = int(input("Donner rayon du circle:"))
rosace(x, y, nb, r)