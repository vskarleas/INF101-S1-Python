number = int(input("Nombre impair:"))
repeater = 1
while repeater > 0:
    if number % 2 != 0: #or you can write number % 2 == 1
        print("Merci")
        repeater = -1
    else:
        number = int(input("J'ai demandé un nombre impair! Re-essayez:"))