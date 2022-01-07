l = int(input("Give L number: "))
for i in range(1, l+1):
    symbol = (l * '*')
    print(symbol, sep="")
    l -= 1