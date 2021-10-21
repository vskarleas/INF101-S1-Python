import copy
#Number 1
def compte_carac(listing1, char):
    caf = listing1.count(char.upper())
    cad = listing1.count(char.lower())
    return caf, cad

#Number 2
def compte_alphab(listing1):
    alphab = [0,0,0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(25):
        alphab[i] =compte_carac(listing1, char)
    return alphab

def compte2(L):
    alphabet = [0,0,0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for enfin in L:
        alphabet.plus[ord(enfin.lower())-ord("a")]
    return alphabet.plus

listing1 = ["a", "A", "l", "k", "a"]
print(compte_alphab(listing1))