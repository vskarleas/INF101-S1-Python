x = str(input("Character: "))
lamda = len(x)
if lamda > 1:
    print("Error, we want only one character")
    exit()
y = ord(x)
if 65 <= y <= 90:
    print("is majuscule")
if 97 <= y <= 122:
    print("is miniscule")
