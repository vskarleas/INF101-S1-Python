#On predit que le programme 1 en ligne 9 va apparaitre en ecran le numero 3 et en ligne 13 va apparaitre 
# en ecran le numero 5

# Programme 1
def increment(a):
    a = a+1

b = 3
increment(b)
print(b)

a = 5
increment(a)
print(a)

a = increment(a)

# Apres on a execute le programme, on a verifie notre prediction
# Si on a place a=increment(a) à la fin du programme (apres print a aussi), le resultat sur notre ecran va etre le meme. 
# Mais, si on met un print(a) apres a=increment(a) de voir qu-est qui est enregistré sur la variable a ou si on utilisera le 
# Python tutor, on voie que maintenat a a enregistré "None". Ca c'est le cas parce que il n'y a pas de "return a" par exemeple sur
# le fonction et donc c'est pourquoi on voie None. Ca, aussu explique pourquoi en ligne 13 on prend comme reposne "5" sur notre
# ecran et non 6 meme si on a appele la fonction "increment"
#----------------------------------------------------------------
#On predit que le programme apres la premier appele, en ligne 33 il va apparaitre sur l'ecran le numero 2, apres
# la deuxieme appel en ligne 36, sur notre ecran il va apparaitre le numero 3 en ligne 37.

# Programme 2
def increment2(a):
    return a+1

b = 1
b = increment2(b)
print(b)

a = increment2(b)
print(a)

# Apres on a execute le programme, on a verifie notre prediction