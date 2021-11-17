repeater = 1
n = float(input("Number: "))
while repeater > 0:
    if n > 0 and n < 30:
        repeater = -1
    else:
        repeater = repeater + 1
        n = float(input("Number: "))

repeater = 1
p = int(input("Pourcentage:"))
while repeater > 0:
    if p < 100 and p > 0:
        repeater = -1
    else:
        repeater = repeater + 1
        p = int(input("Pourcentage:"))

v = n * (p/100)
print(v)
