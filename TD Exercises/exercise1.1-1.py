print("Enter trois reels:")
x = float(input())
y = float(input())
z = float(input())
print("Vous avez saisi", x, "et", y , "et", z)
k = x
x = y
y = z
z = k
print("Apres echange des variables on a:", x , "et", y , "et", z)