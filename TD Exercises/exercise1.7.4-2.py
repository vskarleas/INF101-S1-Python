def function(liste):
    first = liste[0]
    for i in range(1, len(liste)):
        if liste[i] >= first:
            first = liste[i]
        else:
            return False
    return True

def function_dec(liste):
    first = liste[0]
    for i in range(1, len(liste)):
        if liste[i] <= first:
            first = liste[i]
        else:
            return False
    return True

def functioning(liste):
    if function(liste) == False and function_dec(liste) == False:
        return True
    else:
        return False

    