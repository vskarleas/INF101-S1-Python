def moyenne_pondere(notes, coefficients):
    note = 0
    pond =0
    for i in range(len(notes)):
        note = note + (notes[i]*coefficients[i])
    for o in range(len(notes)):
        pond = pond + notes[o]
    result = note / pond
    return result

n = int(input("How many notes? "))
notes=[]
coefficients = []
for k in range(1, n+1):
    print("Give note", k)
    intr = float(input())
    notes.append(intr)
    print("Give coefficient of", k)
    intb = float(input())
    coefficients.append(intb)
final = moyenne_pondere(notes, coefficients)
print("The moyenne pondere is", final)