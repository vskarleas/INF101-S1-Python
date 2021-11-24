from random import *

N = int(input("Donner nombre des personnes: "))
personnes = []
for i in range(1, N+1):
    personnes.append(i)
initial = "I"
dictionary = dict.fromkeys(personnes, initial)
dictionary[1]="C"
final = ""
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
        finalRepeat = repeat
    else:
        repeat = -1

    var = []
    for key in dictionary.keys() :
        var.append(dictionary[key])

    repartition = []
    for e in range(len(var)):
        if var[e] == "I":
            repartition.append(".")
        elif var[e] == "C":
            repartition.append("#")
        elif var[e] == "M":
            repartition.append("*")
    add = repartition[::-1]
    for w in range(len(add)):
        final = add[w] + final
    print(final, sep="\n")



    final = ""
    repartition.clear()
    var = []
    
print(dictionary)

