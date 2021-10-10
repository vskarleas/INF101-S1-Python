def moyenne_pondere(somme, somme2):
    moyenne = (somme/somme2)
    return moyenne

somme = 0
somme2 = 0
nde = float(input("Input:"))
fle = float(input("coeff:"))
for i in range (nde):
    somme = somme + nde * fle
    somme2 = somme2 + fle

print(moyenne_pondere(somme, somme2))
