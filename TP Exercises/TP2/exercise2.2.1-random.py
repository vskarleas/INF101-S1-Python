import random
x = random.randint(1,4)
print(x)

a = int(input("Nombre no1:"))
b = int(input("Nombre no2:"))
if a < b:
    print("Pour a=",a,"et b=",b,"il est vrai que a<b")
    y = random.randint(a, b)
    print(y)
else:
    print("Pour a=",a,"et b=",b,"il est vrai que a>b")