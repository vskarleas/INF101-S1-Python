import random
print("IA aleartoire")
x = int(input("Give a number for the program to search for:"))
g = 1
k = 0
r = 100
print("I search a number between 0 and 100")
a = random.randint(0, 100)
z=0
print("I propose", a)
response = str(input("Enter g if the number is bigger, p if the number is smaller and b if the number is correct: "))
while g > 0:
    if response == "g":
        print("I search a number between",k," and ", a-1)
        r=a-1
        a = random.randint(k, a-1)
        print("I propose", a)
        if a > k:
            k = a
        else: 
            k = k
        response = str(input("Enter g if the number is bigger, p if the number is smaller and b if the number is correct: "))
        g = g + 1
    elif response == "p":
        z=a
        print("I search a number between",z+1," and ", r)
        a = random.randint(z+1, r)
        print("I propose", a)
        if a < r:
            r = r
        else: 
            r = a
        response = str(input("Enter g if the number is bigger, p if the number is smaller and b if the number is correct: "))
        g = g + 1
    elif response == "b":
        print("I won")
        g = 0
    else:
        g = 0
        print("I can't undersatnd, program terminated")