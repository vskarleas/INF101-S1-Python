from turtle import *
def square(cote):
    a = 1
    while a < 5:
        down()
        forward(cote)
        right(90)
        up()
        a = a + 1

def triangle(cote):
    b = 1
    while b < 4:
        down()
        forward(cote)
        right(120)
        up()
        b = b + 1

c = int(input("How may times to see the schemas? "))
cote = 40
distance = cote+10
for kappa in range (0,c):
    square(cote)
    forward(distance)
    triangle(cote)
    forward(distance)
    cote = cote + 15
    distance = cote + 10
