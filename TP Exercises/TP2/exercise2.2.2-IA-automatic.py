import random
print("IA aleartoire")
x = random.randint(0,100)
print("I choose", x)
print("----------")
g = 1
k = 0
r = 100
print("I search a number between 0 and 100")
a = random.randint(0, 100)
z=0
print("I propose", a)
while g > 0:
    if a > x:
        print("I search a number between",k," and ", a-1)
        r=a-1
        a = random.randint(k, a-1)
        print("I propose", a)
        if a > k:
            k = k
        else: 
            k = a
        
        g = g + 1
    elif a < x:
        z=a
        k=z
        print("I search a number between",z+1," and ", r)
        a = random.randint(z+1, r)
        print("I propose", a)
        if a < r:
            r = r
        else: 
            r = a
        
        g = g + 1
    elif a == x:
        print("I won")
        g = 0
    else:
        g = 0
        print("I can't undersatnd, program terminated")