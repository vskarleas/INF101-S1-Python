def dates(a, b, c):
    kappa = 2021 - c
    lam = 12 - b
    kim = 31 - a
    if kappa<0 or lam<0 or kim<0:
        print(a,"/",b,"/",c," n'est pas correct")
    else:
        print(a,"/",b,"/",c," est pas correct")

a = int(input("Donner jour:"))
b = int(input("Donner moi:"))
c = int(input("Donner annee:"))
dates(a, b, c)