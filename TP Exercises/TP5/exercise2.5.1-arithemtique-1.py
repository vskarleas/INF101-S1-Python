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
    for i in range(2, n):
        if n % i == 0:
            N = i
            cap = est_premier(N)
            if cap == True:
                largest_divisor = i
    return largest_divisor

#Main program
n = int(input("Give a number to find the bigest divider: "))
print(plus_grand_diviseur_premier(n))

