def dates(a, b, c):
    kappa = 2021 - c
    lam = 12 - b
    kim = 31 - a
    result = month(b)
    results = result - a
    if kappa>=0 and lam>=0 and kim>=0 and results == kim:
        print(a,"/",b,"/",c," est correct")
    else:
        print(a,"/",b,"/",c," n'est pas correct")

def month(b):
    if b == 2:
        lamda = 28
    else:
        if b%2 != 0:
            lamda = 31
        else:
            lamda = 30
    return lamda

a = int(input("Donner jour:"))
b = int(input("Donner moi:"))
c = int(input("Donner annee:"))
dates(a, b, c)