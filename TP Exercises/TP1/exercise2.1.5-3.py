print("Le quotient")
a = int(input("Donner un nombre:"))
b = int(input("donner un autre nombre:"))
if b == 0 :
    print("Error, division par 0 n'est pas possible")
else :
    print("Le quotient de", a, "par", b, "est:", a // b ," et le reste est", a % b)
