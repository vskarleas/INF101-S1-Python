def function(liste, x):
    if x == liste[i][::1]:
        appartient = True
    else:
        appartient = False
    return appartient

def function(liste, x):
    for i in range(len(liste)):
        if liste[i]==x:
            appartient = True
        else:
            appartient = False
    return appartient

liste = [5, 6, 7]
x = 3
print(function(liste, x))

def function2(liste, x):
    if x in liste:
        appartient = True
    else:
        appartient = False
    return appartient

print(function2(liste, x))

#Exercise 5, 6, 7 are coming soon!!