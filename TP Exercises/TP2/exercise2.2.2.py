import random
x = random.randint(0, 100)
print("--------")
print(x)
y = int(input("Quelle nombre pense toi que le program a choise entre 0 et 100? "))
if y == x:
    print("Gane")
elif y > x:
    print("Trop grand")
else:
    print("Trop petit")