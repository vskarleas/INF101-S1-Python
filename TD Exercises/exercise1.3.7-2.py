print("Somme des n nombres")
somme = 0 
times = int(input("Donner n entiers:"))
while 0 < times < (times + 1) :
    if (times % 2) == 1:
        somme = somme + times
        times = times - 1
    else:
        times = times - 1
print("The somme is:", somme) 