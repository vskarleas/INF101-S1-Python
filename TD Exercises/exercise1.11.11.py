def moyenne_etudiante(etudiant): #etudiant is a dictionary
    name = etudiant['nom']
    moy = etudiant['notes'].values()/len(etudiant['notes'].values())
    return name, moy


def meileur(notes_groupe): #notes_groupe is a list
    best = 0
    bestName = ""
    for i in range(len(notes_groupe)):
        etudiant = notes_groupe[i]
        save = moyenne_etudiante(etudiant)
        if save[1] > best:
            best = save[1]
            bestName = save[2]

