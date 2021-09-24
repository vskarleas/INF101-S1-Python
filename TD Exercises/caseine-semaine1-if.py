print("Banking program")
lancement = str(input("Reply with yes or no:"))
if lancement == "yes":
    guilaume = float(input("Solde du compte de Guillaume?"))
    marion = float(input("Solde du compte de Marion?"))
    if guilaume > 0 and marion > 0:
        print("Tous les deux en positif!")
    elif (guilaume > 0 and marion < 0) or (guilaume < 0 and marion > 0):
        if guilaume > marion :
            print("Marion est en négatif. Guillaume peut lui transférer", -marion, "(il lui restera", guilaume + marion)
        else:
            print("Guilaume est en négatif. Marion peut lui transférer", -guilaume, "(il lui restera", marion + guilaume)
    else:
        print("Tous les deux en négatif! Impossible de rétablir la situation.")
elif lancement == "no":
    print("OK. See you soon!")
else:
    print("There was an error with the system. Please try again. If the problem persists, contact the administrator")