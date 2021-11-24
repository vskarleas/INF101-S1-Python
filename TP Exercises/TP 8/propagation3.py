from random import *

N = int(input("Donner nombre des personnes: "))
personnes = []
for i in range(1, N+1):
    personnes.append(i)
initial = "I"
dictionary = dict.fromkeys(personnes, initial)
dictionary[1]="C"
counter = 1
give = int(input("Nombre des jours: "))
for i in range(give):
    x = randint(1, N)
    y = randint(1, N)
    different = False
    while different != True:
        if x != y:
            different = True
        else:
            different = False
            x = randint(1, N)
            y = randint(1, N)
    first = dictionary.get(x)        
    second = dictionary.get(y)
    if first == "C" and second == "C":
        dictionary[x] = "M"
        dictionary[y] = "M"
    elif first == "C" and second == "I":
        dictionary[x] = "C"
        dictionary[y] = "C"
    elif first == "C" and second == "M":
        dictionary[x] = "M"
        dictionary[y] = "M"
    elif first=="I" and second == "c":
        dictionary[x] = "C"
        dictionary[y] = "C"
        counter = counter + 1
    elif first == "M" and second == "C":
        dictionary[x] = "M"
        dictionary[y] = "M"

moyene = ((counter * N) / give )*100
print(moyene, "%")

