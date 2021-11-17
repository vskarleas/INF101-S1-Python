from random import *
from turtle import *

def creer_liste():
    liste = []
    for i in range(1, 366):
        k = randint(0, 100)
        l = round(k,2)
        liste.append(l)
    return liste

def semaine(liste, day):
    editor = 1
    days = []
    for h in range(48):
        for i in range(7):
            days.append(editor)
            editor = editor +1
        editor = 1
    editor = 1
    for l in range(4):
        for i in range(7):
            days.append(editor)
            editor = editor +1
        editor  = 1
    days.append(1)

    final = 0
    counter = days.count(day)
    for j in range(len(days)):
        if days[j] == day:
            final = final + liste[j]
    result = final / counter

    return result

def final_semain(liste):
    liste_semaine = []
    for i in range(7):
        day  = i+1
        o = semaine(liste,day)
        liste_semaine.append(o)
    return liste_semaine

liste =  creer_liste()
print(final_semain(liste))

def histogram(liste):
    y = final_semain(liste)
    left(90)
    for i in range(len(y)):
        forward(y[i])
        right(90)
        forward(20)
        right(90)
        forward(y[i])
        left(180)  

histogram(liste)


