#MΌταν θέλω να αποθηκεύσω από μια functionδύο πραγματα τα οποία τα έχω
#βάλει στο return, απλά βάζω δύο μεταβλητές που χωρλιζονται με κόμματα.

from random import *
def nb_pile(T):
    c = 0
    for i in range(T):
        if randint(1,2)==1:
            c = c+1
    return c, c/T

def liste_nbpile(N,T):
    liste = []
    for k in range(N):
        lamda = nb_pile(T)
        liste.append(lamda)
    return liste

def compte_parties_xpile(liste_pile, x):
    return liste_pile.count(x)
    
def liste_cpt_parties(N, T):
    liste = []
    alpha = liste_nbpile(N,T)
    for l in range(T+2):
        liste.append(compte_parties_xpile(alpha, l))
    return liste

def liste_cpt_parties_modified(N, T, x):
    #We want to read only one time the list alpha
    liste = liste_nbpile(N,T)
    L = [0]*T
    for l in liste:
        L[l] += 1 
    return L

#Let's do a histogram
    
