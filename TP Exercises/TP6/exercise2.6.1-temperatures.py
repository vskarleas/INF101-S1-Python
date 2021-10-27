def proche_zero(liste):
    listePositive = []
    listeNegative = []
    listeABS = []
    indicator = 0
    for i in range(len(liste)):
        if liste[i] > 0:
            listePositive.append(liste[i])
        elif liste[i] < 0:
            listeNegative.append(liste[i])
        listePositive.sort()
        listeNegative.sort()
        for k in range(len(listeNegative)):
            listeABS.append(abs(listeNegative[k]))
    
    if listePositive[0] > listeABS[0]:
        proche = listeABS[0]
        indicator = 1
    elif listePositive[0] < listeABS[0]:
        proche = listePositive[0]
    elif listePositive[0] == listeABS[0]:
        proche = listePositive[0]
        
    if indicator == 1:
        proche = proche*(-1)
        return proche
    else:
        return proche
        
        
        
        
liste = [3, -2]
print(proche_zero(liste))
