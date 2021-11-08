x = int(input("Nombre max de lettres ? "))
liste = []
result = ''
while x > 0:
    letter = str(input("Lettre :"))
    if letter != "stop":
        liste.append(letter)
        x = x - 1
    else:
        x = -1
for i in range(len(liste)):
    result = result + liste[i]
print(result)
    