def lundi(mot1):
    print(mot1, mot1)

def mardi(mot2):
    omr = True
    final_result = len(mot2)
    while omr == True:
        if final_result % 2 == 1:
            omrt = True #It's impair
            omr = False
        else:
            omrt = False #It's pair
            omr = False
    if omrt == True:
        print(mot2, mot2, mot2, sep=",")
    if omrt == False:
        print(mot2, mot2, mot2, mot2, mot2, mot2, sep="-")

def mercredi(mot3):
    omr = True
    final_result = len(mot3)
    while omr == True:
        if final_result % 2 == 1:
            omrt = True #It's impair
            omr = False
        else:
            omrt = False #It's pair
            omr = False
    if omrt == True:
        print("impair")
    if omrt == False:
        print(mot3)

def jeudi(mot4):
    final_result= len(mot4)
    modulo = final_result % 3
    if final_result % 3 == 0:
        print("")
    else:
        result = (mot4 * modulo)
        print(result)

def vendredi(mot5):
    print(mot5)

def transforme(mot, num_jour):
    if num_jour == 1:
        mot1 = mot
        lundi(mot1)
    elif num_jour == 2:
        mot2 = mot
        mardi(mot2)
    elif num_jour == 3:
        mot3 = mot
        mercredi(mot3)
    elif num_jour == 4:
        mot4 = mot
        jeudi(mot4)
    elif num_jour == 5:
        mot5 = mot
        vendredi(mot5)
    else:
        print("No corresponding date")
    
mot = str(input("Donner un mot:"))
num_jour = int(input("Donner numero de jour:"))
transforme(mot, num_jour)