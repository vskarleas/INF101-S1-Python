def function(liste, x):
    if x == liste[::1]:
        appartient = True
    else:
        appartient = False
    return appartient

def function3(liste, x):
    for i in range(len(liste)):
        if liste[i] == x:
            
            appartient = True
        else:
            appartient = False
            
    return appartient

def function2(liste, x):
    if x in liste:
        appartient = True
    else:
        appartient = False
    return appartient

liste = [5, 6, 7]
x = 5
print(function(liste, x))
print(function3(liste, x))
print(function2(liste, x))

#Exercise 5, 6, 7 on a paper