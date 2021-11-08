x = int(input("Give a number: "))
i = 2
if x > 0:
    while i < x and x % i != 0:
        i = i + 1
    if i == x:
        premier = True
    else:
        premier = False
print(premier)