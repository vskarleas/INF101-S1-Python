from turtle import *

def rosace(x, y, nb, r, t1, tp):
    up()
    speed(100)
    goto(x, y)
    for kapou in range (0, tp):
        for kati in range (0, t1):
            for kappa in range (0, nb):
                down()
                circle(r)
                right(360/nb)
                up()
            forward(4*r)
        goto(x,(y-(4*r)))
        y = y-(4*r)

x = int(input("Donner x:"))
y = int(input("Donner y:"))
nb = int(input("Donner nombre des rosaces:"))
r = int(input("Donner rayon du circle:"))
t1= int(input("Nombre des rosaces dans un ligne:"))
tp= int(input("Nombre des lignes:"))
rosace(x, y, nb, r, t1, tp)