from random import *
def traduire(dictionary, mot):
    for key, value in dictionary.items():
        if mot == key:
            print(mot, "=", value)


def jouerUnMOt(dictionary):
    default = True
    while default == True:
        lab = randint(ord("A"), ord("Z"))
        for keys, values in dictionary.items():
            var = list(keys)
            if chr(lab) == var[0]:
                word = keys
                trad = values
                default = False
    print("=========")
    print("Quelle est la traduction de mot:", word)
    add = str(input("Your answer is: "))
    if add == trad:
        print("C'est correct")
        return 1
    else:
        print("No. La bonne reponse est: ", trad)
        return 0
        
    
#Main programme
score = 0
replay = True
dictionary = {"Bonjour": "Hello", "Bon soir":"Good night", "Salut":"Hello"}
while replay == True:
    lamb = jouerUnMOt(dictionary)
    if lamb == 1:
        score = score + 1
    print("Do you wan tot play again ?")
    choice = str(input("Yes/No ? "))
    if choice == "Yes":
        replay = True
    else:
        replay = False
    print("Your score is", score)
