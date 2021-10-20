def capital_annees(nb_annees, capital_debut):
    repeat = 0
    while repeat < nb_annees:
        capital_debut = (capital_debut * 1.05) - 11
        repeat = repeat + 1
    return capital_debut

def gagne_argent(nb_annees, capital_debut):
    cap=capital_annees(nb_annees, capital_debut)
    if cap < capital_debut:
        gagne = False
    if cap > capital_debut:
        gagne = True
    if cap == capital_debut:
        gagne = False
    return gagne

def placeemnt_min(nb_annees, but):
    caf=capital_annees(nb_annees, but)
    lamda=(caf + 11)/1.05
    return lamda

#Filter out by using the gagne_argent function before it gives the answer
def duree_min(capital, but):
    duration = 1 #in years
    while capital < but:
        capital = (capital * 1.05) - 11
        duration = duration + 1
    nb_annees = duration
    capital_debut = capital
    alfa = gagne_argent(nb_annees, capital_debut)
    if alfa != False:
        return duration

#Main programm
nb_annees = 6
capital_debut = 25
but = 29
capital = 10
print("Possible capital in nb_annees")
print(capital_annees(nb_annees, capital_debut))
print("Capital in nb_annees is bigger on not from the initial capital(capital debut)")
print(gagne_argent(nb_annees,capital_debut))
print("Minimum capital to achieve the 'but' after nb_annees")
print(placeemnt_min(nb_annees, but))
print("Minimum duration to achieve the 'but' starting with specific capital")
print(duree_min(capital, but))
        