def ajoute_suffixe(chaine, suffixe, nb_fois):
    l = (suffixe * nb_fois)
    return l

def ajoute_b(chaine, nb_fois):
    b = ('b' * nb_fois)
    return b

#Program principal
chaine = str(input("Donner un mot: "))
nb_fois = int(input("Donner un nombre: "))
n = ajoute_b(chaine, nb_fois)
print("La fonction ajoute_b appelee avec ces arguments renvoie : ", chaine, n, sep="")
suffixe = str(input("Donner un suffixe: "))
k = ajoute_suffixe(chaine, suffixe, nb_fois)
print("La fonction ajoute_suffixe appelee avec ces arguments renvoie : ", chaine, k, sep="")
