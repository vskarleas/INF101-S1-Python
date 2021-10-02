
x = int(input("Nombre max de lettres ?"))
play = 1
letters = str()
if x == 0:
    exit()
else:
    letter = str(input("Lettre :"))
    while play < x:
        if letter == "stop":
            play = x + 3
        else:
            letters = letters + letter
            letter = str(input("Lettre :"))
            play = play + 1
    letters = letters + letter
    if letters == "0":
        exit()
    else:
        print(letters)
    