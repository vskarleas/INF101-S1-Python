
print("a. Prévisions de stock")
print("b. Stock maximal ")
print("(q pour quitter)")
x = 1
add = str(input())
while x > 0:
    if add == "q":
        x = -1
    elif add == "a":
        n = int(input("Choisissez une semaine : "))
        
        dar = 1024
        lam = (n+2) - n
        print("Semaine 1:", dar)
        while lam <= n:
            if (lam % 4) == 0:
                dar = dar - (lam+20) + 500
                print("Semaine ", lam,": ", dar, sep="")
                lam = lam + 1
            else:
                dar = dar - (lam+20)
                print("Semaine ", lam,": ", dar, sep="")
                lam = lam + 1
        print("a. Prévisions de stock")
        print("b. Stock maximal ")
        print("(q pour quitter)")
        add = str(input())
        x = x + 1
    elif add == "b":
        n = int(input("Choisissez une semaine : "))
        
        dar = 1024
        lam = (n+2) - n
        maximum = 0
        semaine = 0
        while lam <= n:
            if (lam % 4) == 0:
                dar = dar - (lam+20) + 500
                if maximum < dar:
                    maximum = dar
                    semaine = lam
                lam = lam + 1
            else:
                dar = dar - (lam+20)
                if maximum < dar:
                    maximum = dar
                    semaine = lam
                lam = lam + 1
        print("Stock max égal à ", maximum, ", atteint en semaine ", semaine)
        print("a. Prévisions de stock")
        print("b. Stock maximal ")
        print("(q pour quitter)")
        add = str(input())
        maximum = 0
        semaine = 0
        x = x + 1
    else:
        add = str(input("Choix incorrect, recommencez "))
            
            
