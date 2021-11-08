from copy import *
def double_consonne(mot):
    liste = []
    mot = mot.lower()
    for i in range(len(mot)):
        liste.append(mot[i])
    x = 0
    value = False
    liste2 = deepcopy(liste)
    liste2.append("0")
    while x < len(liste):
        k = x
        if liste[x] == liste2[x+1]:
            if not(liste[k] == "a" or liste[k] == "e" or liste[k] == "i" or liste[k] == "u" or liste[k] == "o"):
                final = liste[x]
                value = True
        
        x = x + 1
    return value, final

mot = "ressistant"
print(double_consonne(mot))

def envers(li):
    liste = li[::-1]
    return liste
li=['a', 'b', 'c', 'd']
print(envers(li))