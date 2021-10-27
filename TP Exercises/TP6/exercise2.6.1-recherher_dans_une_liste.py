def minimum(liste):
    minim = 0
    for i in range(len(liste)):
        if liste[i]<minim:
            minim = liste[i]
    return minim

def contient(liste, elem):
    if elem in liste:
        return True
    else:
        return False

def minimum2(liste):
    liste.sort()
    return liste[1]


liste = [1, 4, 6, 3, -2]
elem = -4
print(minimum(liste))
print(contient(liste, elem))
print(minimum2(liste))