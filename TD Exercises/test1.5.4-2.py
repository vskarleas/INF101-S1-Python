repeat = True
while repeat == True:
    x = str(input("Character: "))
    lamda = len(x)
    if lamda > 1:
        print("Error, we want only one character")
        repeat = True
    else:
        y = ord(x)
        if 65 <= y <= 90:
            print("is majuscule")
        if 97 <= y <= 122:
            print("is miniscule")
        choice = str(input("Do you want to play again ? yes/no"))
        if choice == "yes":
            repeat = True
        else:
            repeat = False
print("Program ended")