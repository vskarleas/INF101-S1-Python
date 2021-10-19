
print("Menu, veuillez choisir : ")
print("1. Prévisions adhérents à l'année N (resumé)")
print("2. Prévisions adhérents à l'année N (détails)")
print("3. Adhésions cumulées à l'année N")
print("4. Année à laquelle on obtiendra M adhérents")
print("Q. Quitter")
choice = str(input())
run = True
start_year = 2017
years = 2017
start = 100
checker = 0
somme = 100

while run:
    if choice == "Q":
        print("Au revoir.")
        run = False
    elif choice == "1":
        year = int(input("Choisissez une année :"))
        final_year = year - start_year
        while final_year > 0:
            start = ((start * 8)/100)+start
            final_year = final_year -1
        result = int(start)
        if (start - result) > 0.5:
            result = result + 1
        else:
            result = result + 0
        print("En ", year, "il y a ", result, "adherents.")
        start = 100
        print("Menu, veuillez choisir : ")
        print("1. Prévisions adhérents à l'année N (resumé)")
        print("2. Prévisions adhérents à l'année N (détails)")
        print("3. Adhésions cumulées à l'année N")
        print("4. Année à laquelle on obtiendra M adhérents")
        print("Q. Quitter")
        #run = run + 1
        choice = str(input())
    elif choice == "2":
        year = int(input("Choisissez une année :"))
        if year <= 2017:
            print("En 2017 il y a 100 adherents.")
            print("Menu, veuillez choisir : ")
            print("1. Prévisions adhérents à l'année N (resumé)")
            print("2. Prévisions adhérents à l'année N (détails)")
            print("3. Adhésions cumulées à l'année N")
            print("4. Année à laquelle on obtiendra M adhérents")
            print("Q. Quitter")
            #run = run + 1
            choice = str(input())
        elif year > 2017:
            final_year = year - start_year
            print("En 2017 il y a 100 adherents.")

            while checker < final_year:
                start = start + round(start*0.08)
                result = int(start)
                if (start - result) > 0.5:
                    result = result + 1
                else:
                    result = result + 0
                years = years + 1
                print("En", years, "il y a ", result, "adherents.")
                checker = checker + 1
            start = 100
            years = 2017
            checker = 0
            print("Menu, veuillez choisir : ")
            print("1. Prévisions adhérents à l'année N (resumé)")
            print("2. Prévisions adhérents à l'année N (détails)")
            print("3. Adhésions cumulées à l'année N")
            print("4. Année à laquelle on obtiendra M adhérents")
            print("Q. Quitter")
            #run = run + 1
            choice = str(input())
    elif choice == "3":
        year = int(input("Choisissez une année :"))
        if year <= 2017:
            print("En 2017 il y a 100 adherents.")
        else:
            final_year = year - start_year
            while checker < final_year:
                start = ((start * 8)/100)+start
                result = int(start)
                if (start - result) > 0.5:
                    result = result + 1
                else:
                    result = result + 0
                somme = somme + result
                checker = checker + 1
            start = 100
            checker = 0
            print("De 2017 à ", year, "il y aura ", somme, "adhésions cumulées.")
            print("Menu, veuillez choisir : ")
            print("1. Prévisions adhérents à l'année N (resumé)")
            print("2. Prévisions adhérents à l'année N (détails)")
            print("3. Adhésions cumulées à l'année N")
            print("4. Année à laquelle on obtiendra M adhérents")
            print("Q. Quitter")
            #run = run + 1
            choice = str(input())
    elif choice == "4":
        number = int(input("Entrez le nombre d'adherents voulus: "))
        target_y = 0
        f_nbr = 100
        while f_nbr < number:
            f_nbr = f_nbr + round(f_nbr*0.08)
            target_y += 1
        print("On atteindra",number, "adhérents en",start_year+target_y,".")
        
        # if "100" <= number < "108":
        #     print("On atteindra",number, "adhérents en 2018.")
        # if "108" <= number <"117":
        #     print("On atteindra ",number, " adhérents en 2019.")
        # if "117"<= number < "210":
        #     print("On atteindra ", number, " adherents en 2027.")
        
        if number == "Q":
            print("Au revoir.")
            run = False
        print("Menu, veuillez choisir : ")
        print("1. Prévisions adhérents à l'année N (resumé)")
        print("2. Prévisions adhérents à l'année N (détails)")
        print("3. Adhésions cumulées à l'année N")
        print("4. Année à laquelle on obtiendra M adhérents")
        print("Q. Quitter")
        run = run + 1
        choice = str(input())
    else:
        choice = str(input("Choix invalide, recommencez :"))
        run = run + 1