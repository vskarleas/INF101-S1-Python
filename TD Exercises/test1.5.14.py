def alpha():
    repeat = True
    counter = 1
    x = str(input("Give word: "))
    liste = list(x)
    firstLetter = liste[0]
    if x != "stop":
        while repeat == True:
            x = str(input("Give word: "))
            if x == "stop":
                print(counter)
                repeat = False
            else:
                liste = list(x)
                letter = liste[0]
                if letter > firstLetter:
                    firstLetter = letter
                    counter += 1
                else:
                    print(counter)
                    repeat = False
    else:
        print(0)
alpha()