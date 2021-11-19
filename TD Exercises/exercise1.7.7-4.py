def puissance(n, a):
    res = 1
    if a < 0:
        a = a * (-1)
        for i in range(a):
            res = res * n
        return 1/res
    else:
        res = 1
        for i in range(a):
            res = res * n
        return res

n = 2
a = -6
print(puissance(n, a))
