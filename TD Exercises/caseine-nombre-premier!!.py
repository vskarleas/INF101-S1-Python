
x = int(input("Nombre : "))
i = 2
if x > 0:
    while i < x and x % i != 0:
        i = i +1
    if i == x :
        est_premier = True
    else :
        est_premier = False
    
    if est_premier:
        print(x, "est premier.")
    else:
        print(x, "n'est pas premier.")