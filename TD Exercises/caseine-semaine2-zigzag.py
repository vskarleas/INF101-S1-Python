
x = int(input("Numero de debut:"))
y = int(input("Numero de fin:"))
z = int(input("Nombre de z:"))
klr = ('z' * z)
z = x
k = y
if x == y :
    print(f" {x} {klr}zigzag")
if x > 0 and y > 0 and x != y:
    while x < y+1:
        if x <= y:
            print(f"{klr}zigzag {x}")
            x = x + 1
            print(f" {x} {klr}zigzag")
            x = x + 1
        if z > k:
            print("Rien ne s'affiche car ", x ,">", y)
            x = y + 1
if x < 0 and y > 0:
    while x < y:
        if x <= y:
            print(f" {x} {klr}zigzag")
            x = x + 1
            print(f"{klr}zigzag  {x}")
            x = x+1
        if z > k:
            print("Rien ne s'affiche car ", x ,">", y)
            x = y + 1
    print(f" {y} {klr}zigzag")
if x < 0 and y < 0 and x < y:
    while x < y:
        print(f"{x} {klr}zigzag")
        x = x +1
        print(f"{klr}zigzag  {x}")
        x = x+1
if x < 0 and y < 0 and x > y:
    print("Rien ne s'affiche car ", x ,">", y)