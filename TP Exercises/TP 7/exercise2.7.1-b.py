def tri_insertion(liste):
    maxi = []
    for i in range(len(liste)):
        t = min(liste)
        maxi.append(t)
        liste.remove(t)
    return maxi