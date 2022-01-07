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

def function3Corrected():
    liste = []
    repeat = True
    firstNumber = int(input("Add number: "))
    liste.append(firstNumber)
    if firstNumber != -1:
        while repeat == True:
            x = int(input("Add number: "))
            if x == -1:
                repeat = False
            else:
                repeater = True
                while repeater == True:
                    if x == (firstNumber +1):
                        liste.append(x)
                        firstNumber = x
                        repeater = False
                    else:
                        print("You need to add the number one by one. Th eprevious number is ",firstNumber,". Try again beow.")
                        x = int(input("Add number: "))
                        repeater = True
        return liste
    else:
        return liste


#Main program
liste = function3Corrected()
melange = function(liste)
position = function2(liste, melange)
counter = 1
while position != 0:
    melange = function(liste)
    position = function2(liste, melange)
    counter = counter +1
print(counter)