l = int(input("Give L number: "))
spaces = 0
for i in range(1, l+1):
    symbol = (l * '*')
    symbol2 = (spaces * ' ')
    print(symbol2, symbol, sep="")
    l -= 1
    spaces += 1