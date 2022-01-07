etu = 30
final = 0
best = 0
somme = 0
for studentID in range (1, etu+1):
    print("For student ", studentID)
    for i in range(1,11):
        print("Note ",i,":")
        note=int(input())
        somme = somme + note
    result = somme /10
    print("Moyenne of student no", studentID, "is:", result)
    final = final + result
    if best <= result:
        best = result
        theBest = studentID
finals = final/etu
print("----------")
print("The moyenne of all students (",etu,") is:", finals)
print("The student no", theBest, "had the best moyenne which was:", best)