print("Le quotient")
a = int(input("Donner un nombre:"))
b = int(input("donner un autre nombre:"))
c = int(input("donner un troisieme nombre:"))
if 1 <= a <= 6 :
    print("la valeur du premier de est correct")
    if 1 <= b <= 6 :
        print("la valeur du deuxieme de est correct")
        if 1 <= c <= 6 :
            print("la valeur du deuxieme de est correct")
            if a > b:
                if b > c:
                    print(" les classes decroissantes sont:", a, b, c)
                else :
                    print(" les classes decroissantes sont:", a, c, b)
            else :
                if a > c:
                    print(" les classes decroissantes sont:", b, a, c)
                else :
                    if b > c:
                        print(" les classes decroissantes sont:", b, c, a)
                    else:
                        print(" les classes decroissantes sont:", c, b, a)
        else :
            print("la valeur n'est pas bon")
    else :
        print("la valeur n'est pas bon")
else :
     print("la valeur n'est pas bon")
    
