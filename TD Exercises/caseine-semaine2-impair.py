omr = True
number = int(input("Add an impair number: "))
while omr == True:
    if number % 2 == 1:
        print("Merci")
        omr = False
    else:
        number = int(input("J'ai demandé un nombre impair! Re-essayez: "))



