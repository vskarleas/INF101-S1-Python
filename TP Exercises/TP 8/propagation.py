from random import *

N = int(input("Donner nombre des personnes: "))
personnes = []
for i in range(1, N+1):
    personnes.append(i)
initial = "I"
dictionary = dict.fromkeys(personnes, initial)
dictionary[1]="C"
repeat = 1
while repeat > 0:
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
    elif first == "M" and second == "C":
        dictionary[x] = "M"
        dictionary[y] = "M"

    logic = any(x == "C" for x in dictionary.values())
    if logic == True:
        repeat = repeat + 1
    else:
        repeat = -1

res = []
muets = 0
ignor = 0
for key in dictionary.keys() :
    res.append(dictionary[key])
for l in range(len(res)):
    if res[l] == "M":
        muets = muets + 1
    else:
        ignor = ignor + 1

print("Nombre d'ignorants: ", ignor)
print("Nombre des muets: ", muets)



print(dictionary)
