def ajoute_suffixe(chaine, suffixe, nb_fois):
    l = (suffixe * nb_fois)
    print(chaine, l, sep="")


#principal program
chaine = "hello"
suffixe = "you"
nb_fois = 3
ajoute_suffixe(chaine, suffixe, nb_fois)
