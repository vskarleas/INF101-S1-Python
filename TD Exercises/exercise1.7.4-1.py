def function(liste):
    first = liste[0]
    for i in range(1, len(liste)):
        if liste[i] > first:
            first = liste[i]
        else:
            return False
    return True

liste=[1,4,6,8,9,0]
print(function(liste))