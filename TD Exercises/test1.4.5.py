def sommeChifre(x):
    liste = list(str(x))
    somme = 0
    for i in range(len(liste)):
        somme = somme + int(liste[i])
    print(somme)
x = int(input("Give a number: "))
print("His somme is")
sommeChifre(x)