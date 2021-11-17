def tri_insertion(tab): 
    liste = []
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j+1] = tab[j] 
                j = j - 1
        tab[j + 1] = k
    return tab
# Programme principale pour tester le code ci-dessus

tab = [98, 22, 15, 32, 2, 74, 63, 70]
print ("Le tableau trié est:")
print(tri_insertion(tab))