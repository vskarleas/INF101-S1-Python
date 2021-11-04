print("Nombres premiers")
n = int(input("Add entier N positif:"))
play = 2
i = 2
choise = "yes"
while play > 1:
    if n < 0:
        print("This is not a postif N, try again")
        n = int(input("Add entier N positif:"))
    else:
        while i < n and (n%i) != 0:
            i = i + 1
        if i == n:
            omr = 200 #This is an ID for success response 
        else:
            omr = 250 #This is an ID for wrong response 
        
        if omr == 200 :
            print("The number", n, "is premier")
            print("Do you want to play again ?")
            choising = str(input("Reply with yes or no:"))
            if choising == choise:
                play = play + 1
                n = int(input("Add entier N positif:"))
            else:
                play = 0
        else:
            print("This is not a premier number")
            print("Do you want to play again ?")
            choising = str(input("Reply with yes or no:"))
            if choising == choise:
                play = play + 1
                n = int(input("Add entier N positif:"))
            else:
                play = 0
print("The game is terminated")
