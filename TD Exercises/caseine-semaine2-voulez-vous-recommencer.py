print("Voulez vous recommencer program")
choise = "yes"
number = float(input("Give a number: "))
while choise == "yes":
    print("The number", number, "to the power of 2 is", (number **2))
    choising = str(input("Do you want to continue to play? yes or no? "))
    if choising == "yes" or choising == "no":
        if choising == choise:
            choise = "yes"
            number = float(input("Give a number: "))
        else:
            choise = "no"
    else:
        print("ERROR! Please reply with only yes or no.")
        choising = str(input("Do you want to continue to play? yes or no? "))
        if choising == "yes":
            choise = "yes"
            number = float(input("Give a number: "))
        elif choising == "no":
            choise = "no"
        else:
            print("We couldn't understand your answer.")
            choise = "no"

print("The game is terminated. Thank you!")