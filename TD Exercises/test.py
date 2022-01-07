l = int(input("Give L number: "))
default = 1
for i in range(1, l+1):
    symbol = (default * '*')
    print(symbol)
    default += 1