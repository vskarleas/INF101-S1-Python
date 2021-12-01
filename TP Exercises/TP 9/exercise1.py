from copy import *
def ajoutemot(dfren, mfr, wen):
    dfren[mfr]=wen


def suprrimeMot(dictionary, mot):
    dictionary.pop(mot, None)
    

def afficheDeco(dictionary):
    for key, value in dictionary.items():
        print(key, "=", value)

def afficheDecoLettre(dictionary, lettre):
    copyDictionary = deepcopy(dictionary)
    for keys, values in copyDictionary.items():
        var = list(keys)
        if lettre not in var[0]:
            print(keys, "=", values)

def afficheDecoLongeur(dictionary, number):
    copyDictionary = deepcopy(dictionary)
    for keys, values in copyDictionary.items():
        var = list(keys)
        if number == len(var):
            print(keys, "=", values)

#Principal programme
fr = {"Bonjour": "Hello", "Chat": "Cat", "Petit-dejeuner":"Breakfast"}
print("Time to add some elements into the dictionary")
mot = str(input("Add the word that you want to be deleted: "))
suprrimeMot(fr, mot)
afficheDeco(fr)

