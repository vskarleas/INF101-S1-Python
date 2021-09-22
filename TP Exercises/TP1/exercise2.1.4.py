text = input("Donner  entier no1:")
x = int(text)
text = input("donner un entier no2:")
y = int(text)
z = x - y
if z < 0:
    res = -z
else:
    res = z
print("valeur absolu:", res)
