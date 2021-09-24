x = int(input("From where do you want to start your zigzag snake? Number: "))
y = int(input("Where do you want to end your zigzag snake? Number: "))
z = int(input("How many Zs do you want to include ? "))
z = x
k = y
klr = 'z'*z
while x != y+1:
    if x <= y:
        print(klr, "igzag", x, sep="")
        x = x + 1
        print(x, klr, "igzag", sep="")
        x = x + 1
    if z > k:
        print("Rien ne s'affiche car ", x ,">", y)
        x = y + 1