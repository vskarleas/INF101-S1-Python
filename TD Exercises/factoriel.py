n = int(input("n=?"))
result = 1
if n < 0:
    print("La factorielle n'est pas definie pour les nombres négatifs.")
elif n == 0:
    print("La factorielle de 0 vaut 1 .")
else:
    k = n
    while n > 0:
        result = result*n
        n = n -1
    print(f"La factorielle de {k} vaut {result}.")