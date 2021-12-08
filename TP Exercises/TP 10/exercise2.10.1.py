def ajouter(dico, clef):
    copie = dict(dico)
    copie[clef] = 0
    return copie

    d = {'a': 12, 'b': 25}
    d_avec = ajouter(d, 'c')