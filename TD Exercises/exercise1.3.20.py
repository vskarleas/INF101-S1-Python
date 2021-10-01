n = int(input("Give a number n:"))
pyramide = 7
spacing = 0
for pyramide in range (1, pyramide+1):
    klr = ('^' * n)
    spaces = (' ' * spacing)
    spaces1 = (' ' * n)
    n = n +1
    spacing = n
    print(f"{spaces1}{klr}{spaces}{klr}{spaces1}")