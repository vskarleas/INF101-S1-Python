# Programme 1
def est_solution(x, a, b, c):
    y = a * x ** 2 + b * x + c
    if y == 0:
        rep=True
    else:
        rep=False
    return rep

rep = est_solution(1, 1, -2, 1)
print(rep)
print(est_solution(5, 2, -20, 50))
print(est_solution(2.5 , 1, 2, 3))

# Programme 2
def distance(xA, yA, xB, yB):
    d = (xB-xA)**2+(yB-yA)**2
    d = d**(1/2)
    return d

def appartient_cercle(xA, yA, rayon):
    if distance(0, 0, xA, yA) == rayon:
        return True
    else:
        return False

d = distance(1, 2, 2, 1)
print(d)

rep = appartient_cercle(1, 1, 2)
print(rep)

print(appartient_cercle(1, 0, 1))

# Programme 1
# Valeurs des arguments (on a trois appels):
# En premier appel (ligne 10) sont: 1 pour x, 1 pour a, -2 pour b, 1 pour c (resulat donne à ligne 11)
# En deuxieme appel (ligne 12) sont: 5 pour x, 2 pour a, -20 pour b et 50 pour c
# En troisieme appel (ligne 13) sont: 2.5 pour x, 1 pour a, 2 pour b et 3 pour c

# Valeur des retours
# Pour appel no 1 (ligne 11) la valeur de retour est "True"
# Pour appel no 2 (ligne 12) la valeur de retour est "True"
# Pour appel no 3 (ligne 13) la valeur de retour est "False"


#Programme 2
# Valeurs des arguments (on a trois appels):
# En premier appel (ligne 27) sont: 1 pour xA, 2 pour yA, 2 pour xB, 1 pour yB ce sont des parametres seulement en function "distance" (resulat donne à ligne 28)
# En deuxiemme appel (ligne 30) sont: 1 pour xA, 1 pour yA et 2 pour rayon ce sont des parametres seulemnt en function "appartient_cercle" (results donne à ligne 31)
#  En trosime appel (ligne 33) sont: 1 pour xA, 0 pour yA et 1 pour rayon ce sont des parametres seulemnt en function "appartient_cercle"

# Valeur des retours
# Pour appel no 1 (ligne 27) la valeur de retour est "1.4142135623730951"
# Pour appel no 2 (ligne 30) la valeur de retour est "False"
# Pour appel no 3 (ligne 33) la valeur de retour est "True"