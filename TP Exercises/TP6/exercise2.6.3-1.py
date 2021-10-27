def alphabet(n):
    liste1=[]
    #In this list we will create the alphabet so that we 
    #are sure that it's not a notation and this way is 
    #accepted on the exams as well
    for i in range(ord("a"), ord("z")+1):
        liste1.append(chr(i))

    liste2=[]
    for k in range(ord("A"), ord("Z")+1):
        liste2.append(chr(k))

    if n in liste1:
        position = liste1.index(n)
        position = position + 1
    elif n in liste2:
        position = liste2.index(n)
        position = position + 1
    elif n == " ":
        position = 0
    else:
        position = -1
    return position

def chifremment(mot):
    final = []
    cad = list(mot)
    for i in range(len(cad)):
        n = cad[i]
        caf = alphabet(n)
        final.append(caf)
    print(*final, sep="+")


def chifremment2(mot):
    final = []
    cad = list(mot)
    for i in range(len(cad)):
        n = cad[i]
        caf = alphabet(n)
        if caf == 0:
            final.append(" ")
        elif caf == -1:
            final.append(n)
        else:
            caf = str(caf)+"+" #Here I need to do something different so that it doesn't appear the +every time. Or, make something that will remove it before space
            final.append(caf)
        
        #for h in range(len(final)):
            #if final[h+1] == 0:
                #final.remove[h]
                #final.append(final[h]-"+")
            #else:
                #final
    print(*final, sep="")


# Principal program
play = 1
while play > 0:
    mot = str(input("Donner un text: "))
    chifremment2(mot)
    choice = str(input("Do you want to play again ? yes / no :"))
    if choice == "yes":
        play = play + 1
    else:
        play = -1