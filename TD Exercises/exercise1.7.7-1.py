def factorielle(x):
    res = 1
    for i in range(x):
        res = res * x
        x = x - 1
    return res

print(factorielle(5))