lines = int(input("Donner un entier L:"))
print("Figure a")
linesb = lines
lining = 1
lining3 = 1
spacing = lines
lining4 = lines
lining5 = lines
lining6 = (lines+1) - lines
lining7 = lines-1
for lines in range (1, lines+1):
    print("****")

print("Figure b")
for linesb in range (1, linesb+1):
    while lining <= linesb:
        klrc = ('*' * lining)
        print(klrc)
        lines = lines - 1
        lining = lining + 1
print("Figure c")
for linesb in range (1, linesb+1):
    while lining3 <= linesb:
        klrd = ('*' * lining3)
        space = (' ' * spacing)
        print(f"{space}{klrd}")
        lines = lines - 1
        spacing = spacing -1
        lining3 = lining3 + 1
print("Figure d")
for linesb in range (1, linesb+1):
    klrb = ('*' * lining5)
    print(klrb)
    lining5 = lining5 - 1
print("Figure e")
for linesb in range (1, linesb+1):
    klrb = ('*' * lining4)
    space4 = (' ' * spacing)
    print(f"{space4}{klrb}")
    spacing = spacing +1
    lining4 = lining4 - 1
print("Figure f")
for linesb in range (1, linesb):
    klrk = ('*' * lining6)
    spacing6 = (' ' * lining7)
    print(f"{spacing6}{klrk}{spacing6}")
    spacing = spacing +1
    lining7 = lining7 - 1
    lining6 = lining6 + 2
png = int(lining6/2)
opn = ('*' * png)
print(f"{opn}o{opn}")