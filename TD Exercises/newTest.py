from random import *
def code4(mot):
    word = list(mot)
    indice = len(word)
    new = []
    while indice >0:
        if indice >0:
            a = randint(0, indice-1)
            new.append(word[a])
            word.pop(a)
            indice = indice - 1
    return "".join(new)

print(code4("newbie"))