def compte2(seq):
    liste = list(seq)
    dictionary = {}
    for i in range(1, len(liste)):
        var = liste[i-1]+liste[i]
        if var in dictionary:
            dictionary[var]=dictionary[var]+1
        else:
            dictionary[var]=1
    return dictionary

#correction
def comptE2(seq):
    dictionary = {}
    for i in range(len(seq)-1):
        c = seq[i]+seq[i+1] #or we can say seq[i:i+1]
        if c in dictionary:
            dictionary[c]= dictionary[c] +1
        else:
            dictionary[c]=1
    return dictionary

def compten(seq, n):
    liste2 = list(seq)
    liste = []
    for i in range(n):
        liste.append(liste2[i])
    dictionary = {}
    for i in range(1, len(liste)):
        var = liste[i-1]+liste[i]
        if var in dictionary:
            dictionary[var]=dictionary[var]+1
        else:
            dictionary[var]=1
    return dictionary

#Principal program
dna = input("Add DNA sequence :")
d2 = compte2(dna)
print(d2)
print(compten(dna, 3))

seq = "ACCTAGCCCTA"
n = 7
print(compten(seq, n))