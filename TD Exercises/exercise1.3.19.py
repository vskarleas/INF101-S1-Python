etu = 30
final = 0
best = 0
etud = (etu+1)-etu
for etu in range (1, etu+1):
    note1=int(input("Note 1:"))
    note2=int(input("Note 2:"))
    note3=int(input("Note 3:"))
    note4=int(input("Note 4:"))
    note5=int(input("Note 5:"))
    note6=int(input("Note 6:"))
    note7=int(input("Note 7:"))
    note8=int(input("Note 8:"))
    note9=int(input("Note 9:"))
    note10=int(input("Note 10:"))
    z = (note1 + note2 + note3 + note4 + note5 + note6 + note7 + note8 + note9 +note10)/10
    print("Moyenne of student no", etud, "is:", z)
    final = final + z
    if best <= z:
        best = z
        theBest = etud
    etud = etud + 1
finals = final/etu
print("----------")
print("The moyenne of all students (",etu,") is:", finals)
print("The student no", theBest, "had the best moyenne which was:", best)