l = int(input("Give L number: "))
default = 1
spaces = l-1
for i in range(1, l+1):
    symbol = (default * '*')
    symbo2 = (spaces * ' ')
    print(symbo2, symbol, sep="")
    default += 1
    spaces -= 1