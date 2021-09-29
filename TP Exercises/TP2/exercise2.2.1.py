from math import *
a = float(input("Entrez la langeur de l'hypothenuse: "))
h = float(input("Entrez la valeur d'un angle (radians): "))
z = pi - h #Calculates the somme of the two other angles
adj = cos(a) * h
opp = sin(a) * h
if (h ** 2 == (adj ** 2) + (opp ** 2)):
    print("Le Pythagore est correct pour cet triangle")
else:
    print("Le pythagore n'est pas correct pour les valeurs qui ont donne")
print("----------")
print("programme d'equiation ax^2 + bx + c")
a = int(input("Entrez valeur pour a: "))
b = int(input("Entrez valeur pour b: "))
c = int(input("Entrez valeur pour c: "))
g = 1
delta = (b ** 2) - (4*a*c)
while g > 0:
    if delta >= 0:
        s1 = (-b + sqrt(delta))/2*a
        s2 = (-b - sqrt(delta))/2*a
        print("l'equation", a,"x^2+",b,"x+",c,"a comme racines, s1=", s1, "et s2=", s2)
        print("est que tu veux de le refaire ?")
        choice = str(input("oui ou non:"))
        if choice == "oui":
            a = int(input("Entrez valeur pour a: "))
            b = int(input("Entrez valeur pour b: "))
            c = int(input("Entrez valeur pour c: "))
            delta = (b ** 2) - (4*a*c)
            g = g + 1
        else:
            i = g
            g = 0
    else:
        print("L'equation n'a pas des solutions")
        print("est que tu veux de le refaire ?")
        choice = str(input("oui ou non:"))
        if choice == "oui":
            a = int(input("Entrez valeur pour a: "))
            b = int(input("Entrez valeur pour b: "))
            c = int(input("Entrez valeur pour c: "))
            delta = (b ** 2) - (4*a*c)
            g = g + 1
        else:
            i = g
            g = 0
print("Programme termine. Tu as utilise le programme ", i, "fois")
