def puissance(n, a):
    res = 1
    for i in range(a):
        res = res * n
    return res

n = -2
a = 2
print(puissance(n, a))
