def depasse(A):
    n = 1
    for k in range(2, A + 1):
        n *= k
    return n
