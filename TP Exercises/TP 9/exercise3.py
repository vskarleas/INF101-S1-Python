from random import *
def initPlayers(playersNumber):
    players = []
    id = 1
    for id in range(playersNumber):
        name = str(input('Name of player ' + str(id+1) + ': '))
        players.append(name)
    return players

def initScores(players,v=0):
    if v != 0:
        dictionary = dict.fromkeys(players, v)
    else:
        dictionary = dict.fromkeys(players, 0)
    return dictionary

def selectWords(dictionary, wordsNumber):
    words = []
    translastions = []
    while wordsNumber > 0:
        lab = randint(ord("A"), ord("Z"))
        for keys, values in dictionary.items():
            var = list(keys)
            if chr(lab) == var[0]:
                words.append(keys)
                translastions.append(values)
                wordsNumber = wordsNumber -1
    return words, translastions

def newDict(words, translations):
    lamdao = zip(words, translations)
    newDictionary = dict(lamdao)
    return newDictionary

def jouer(newDictionary, score):
    default = True
    while default == True:
        playerScore = 0
        for key, value in score.items():
            print("==========")
            print("It's ", key," turn.")
            for word, trad in newDictionary.items():
                print("Your word is: ", word)
                answer = str(input("Which is its translation ?"))
                if answer == trad:
                    print("C'est correct")
                    playerScore += 1
                else:
                    print("No. La bonne reponse est: ", trad)
            score[key]=playerScore
            playerScore = 0
        print("Do you want to play again ?")
        choice = str(input("yes/no ?" ))
        if choice == "yes":
            default = True
        else:
            default = False
    return score

def top(score, wordsNumber):
    playersFinal = []
    scoreFinal = []
    pourcentage = []
    for key, value in score.items():
        playersFinal.append(key)
        scoreFinal.append(value)
    top = max(scoreFinal)
    index = scoreFinal.index(top)
    return playersFinal[index], top

def pourcentage(score, wordsNumber):
    playersFinal = []
    scoreFinal = []
    pourcentage = []
    for key, value in score.items():
        playersFinal.append(key)
        scoreFinal.append(value)
    for i in range(len(playersFinal)):
        pour = scoreFinal[i]*100/wordsNumber
        pourcentage.append(pour)
    for k in range(len(playersFinal)):
        print(playersFinal[k], ": ", pourcentage[k])



 

playersNumber = int(input("How many players ?"))
players = initPlayers(playersNumber)
score = initScores(players, v=0)
wordsNumber = int(input("How many words do you you want for every round? "))
dictionary = {"Bonjour": "Hello", "Bon soir":"Good night", "Salut":"Hello"}
var = selectWords(dictionary, wordsNumber)
words = var[0]
translations = var[1]
newDictionary = newDict(words, translations)
finalScore = jouer(newDictionary, score)
best = top(score, wordsNumber)
name = best[0]
bestScore = best[1]
print("The top player is", name,"with score ", bestScore)
pourcentage(score, wordsNumber)