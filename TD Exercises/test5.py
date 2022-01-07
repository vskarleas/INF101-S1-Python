l = int(input("Give L number: "))
default = 1
spaces = l -1
for i in range(1, l):
    symbol = (default * '*')
    symbol2 = (spaces * ' ')
    print(symbol2, symbol, symbol2, sep="")
    default += 2
    spaces -= 1
symbol = (int(default/2 )* '*')
print(symbol,"o",symbol,sep="")