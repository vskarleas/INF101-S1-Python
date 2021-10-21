#There is also a much more simple way
def alpha(word):
    caracter = "0"
    counter = 1
    repeat = 1
    while repeat > 0:
        while word != "stop":
            if word[:1:1] != caracter and repeat != 0:
                caracter = word[:1:1]
                word = input("Donner un mot:")
                if word[:1:1] > caracter:
                    counter = counter + 1
                    repeat = repeat + 1
                else:
                    print(counter)
                    break
            else:
                word = input("Donner un mot:")
                repeat = repeat + 1
        if word == "stop":
            print("Program is ended") #we can add also break 
        repeat = 0

word = input("Donner un mot:")
alpha(word)
