lines = int(input("Donner un entier L:"))
print("Figure A")
keepLines = lines
figureB = 1
figureC = 1
figureD = lines
figureE = lines
figureF = (lines+1) - lines
spacesF = lines-1

spacing = lines

for lines in range (1, lines+1):
    print("****")

print("----------")
print("Figure B")
for keepLines in range (1, keepLines+1):
    while figureB <= keepLines:
        klrc = ('*' * figureB)
        print(klrc)
        lines = lines - 1
        figureB = figureB + 1
print("----------")
print("Figure C")
for keepLines in range (1, keepLines+1):
    while figureC <= keepLines:
        klrd = ('*' * figureC)
        spaceC = (' ' * spacing)
        print(f"{spaceC}{klrd}")
        lines = lines - 1
        spacing = spacing -1
        figureC = figureC + 1
print("----------")
print("Figure D")
for keepLines in range (1, keepLines+1):
    klrb = ('*' * figureD)
    print(klrb)
    figureD = figureD - 1
print("----------")
print("Figure E")
for keepLines in range (1, keepLines+1):
    klrb = ('*' * figureE)
    spaceE = (' ' * spacing)
    print(f"{spaceE}{klrb}")
    spacing = spacing +1
    figureE = figureE - 1
print("----------")
print("Figure F")
for keepLinesg in range (1, keepLines):
    klrk = ('*' * figureF)
    spaceF = (' ' * spacesF)
    print(f"{spaceF}{klrk}{spaceF}")
    spacing = spacing +1
    spacesF = spacesF - 1
    figureF = figureF + 2
png = int(figureF/2)
opn = ('*' * png)
print(f"{opn}o{opn}")