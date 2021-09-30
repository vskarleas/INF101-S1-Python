n = int(input("Add a number:"))
choising = "yes"
a = 0
b = 1
while choising == "yes":
    a = 0
    b = 1
    if n > 0:
        for n in range (1, n):
            c = a + b
            a = b
            b = c
        print("The fibonacci number is", c)
        choice = str(input("Do you want to try again ? yes/no:"))
        if choice == "yes":
            choising = "yes"
            n = int(input("Add a number:"))
        else:
            choising = "no"
    elif n == 0 or n == 1:
        print("The fibonacci number is", b)
        choice = str(input("Do you want to try again ? yes/no:"))
        if choice == "yes":
            choising = "yes"
            n = int(input("Add a number:"))
        else:
            choising = "no"
    else:
        print("I can't calculate the fibonacci number without a positif number")
        choice = str(input("Do you want to try again ? yes/no:"))
        if choice == "yes":
            choising = "yes"
            n = int(input("Add a number:"))
        else:
            choising = "no"
print("Bye bye")