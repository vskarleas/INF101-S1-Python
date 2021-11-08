def NextElem(elm, liste):
    if len(liste)>2:
        if elm in liste:
            lamda = liste.index(elm)
            if lamda+1 == len(liste):
                final = liste[0]
            else:
                final = liste[lamda+1]
            return final
        else:
            return

liste=['a','b','c']
elm = 'd'
print(NextElem(elm, liste))