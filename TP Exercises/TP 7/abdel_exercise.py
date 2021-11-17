def derniere_consone(mot):
    liste = list(mot)
    voyelle = ["a", "e", "i", "o", "u"]
    for i in range(len(liste)):
        if liste[i] not in voyelle:
            index = i
            consonne = liste[i]

    return index, consonne

mot = "arrivee"
print(derniere_consone(mot))


def derniere_consone2(mot):
    liste = list(mot)
    index = []
    consonne = []
    voyelle = ["a", "e", "i", "o", "u"]
    for i in range(len(liste)):
        if liste[i] not in voyelle:
            index.append(i)
            consonne.append(liste[i])

    return index[-1], consonne[-1]

mot = "arrivee"
print(derniere_consone2(mot))

