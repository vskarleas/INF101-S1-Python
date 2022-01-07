def factorielle(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n -1
    return result

def coeff_binomeial(n,k):
    res1 = factorielle(n)
    res2 = factorielle(k)
    res3 = factorielle(n-k)
    result = res1 / (res2 * res3)
    return int(result)

def traingle_pascal(nb_lignes):
    k = 0
    n = 1
    liste = []
    print(1)
    while n<nb_lignes:
        while n>=k:
            liste.append(coeff_binomeial(n,k))
            k += 1
        print(' '.join(str(x) for x in liste))
        liste.clear()
        k=0
        n += 1


traingle_pascal(7)