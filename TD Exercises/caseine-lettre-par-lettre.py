
x = int(input("Nombre max de lettres ? "))
play = 1
letters = ""
if x > 0:
    letter = str(input("Lettre :"))
    while play < x:
        if letter == "stop":
            play = x + 3
        else:
            letters = letters + letter
            letter = str(input("Lettre :"))
            play = play + 1
    if letter != "stop":
        letters = letters + letter
    if letters == "0":
        exit()
    else:
        print(letters)
if x == 0:
     exit()
    