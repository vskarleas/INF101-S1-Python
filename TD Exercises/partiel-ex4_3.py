def erreurs(secret, essais):
    L = []
    for i in range(len(essais)):
        if essais[i] not in secret:
            L.append(essais[i])
    return L

secret="CHATEAU"
essais=["E", "A", "X", "R", "T", "S"]
print(erreurs(secret, essais))