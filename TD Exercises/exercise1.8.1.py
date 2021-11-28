from copy import *
from random import *
def function(liste):
    l = []
    for i in range(len(liste)):
        j = randint(0, len(liste)-1)
        l.append(liste[j])
        liste.pop(j)
    return l

def function2(l1, l2):
    counter = 0
    if len(l1) == len(l2):
        for i in range(len(l1)):
            if l2[i] == l1[i]:
                counter = counter + 1
    return counter

def function3():
    liste = []
    repeat = True
    while repeat == True:
        x = int(input("Enter entier: "))
        if x != -1 and x >= 0:
            liste.append(x)
            repeat = True
        else:
            repeat = False
    return liste

#Main program
liste = function3()
melange = function(liste)
position = function2(liste, melange)
counter = 1
while position != 0:
    melange = function(liste)
    position = function2(liste, melange)
    counter = counter +1
print(counter)

