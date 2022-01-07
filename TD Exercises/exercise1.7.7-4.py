def puissance(n, a):
    res = 1
    if a < 0:
        for i in range(abs(a)):
            res = res * n
        return 1/res
    else:
        for i in range(a):
            res = res * n
        return res

n = 2
a = -3
print(puissance(n, a))
