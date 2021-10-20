def est_premier(N):
    i = 2
    if N > 0:
        while i < N and N % i != 0:
            i = i +1
        if i == N :
            est_premier = True
        else :
            est_premier = False
    return est_premier

def plus_grand_diviseur_premier(n):
    largest_divisor = 0
    listing =[]
    for i in range(2, n):
        if n % i == 0:
            N = i
            cap = est_premier(N)
            if cap == True:
                largest_divisor = i
                listing.append(largest_divisor)
    return listing

def pgcd(a , b):
    o=1
    n = a
    alfa = plus_grand_diviseur_premier(n)
    n = b
    lamda = plus_grand_diviseur_premier(n)
    if len(alfa)>len(lamda):
        h = len(lamda)
    elif len(alfa)<len(lamda):
        h = len(alfa)
    else:
        h = len(alfa)
    for k in range(0, h):
        if alfa[o-1:o:1] == lamda[o-1:o:1]:
            commun = alfa[o-1:o:1]
        o = o + 1

    return commun[0]


#Main program
a = int(input("Give a first number to find the bigest divider: "))
b = int(input("Give a second number to find the bigest divider: "))
if a != 0 and b !=0:
    print(pgcd(a, b))


