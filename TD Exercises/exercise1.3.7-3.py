print("Somme des n nombres lus au clavier")
somme = 0 
n = 0
times = int(input("How many numbers do you wan tto claculate ?"))
if times < 0:
    print("It's impossible to calculate the somme of", times, "numbers")
else:
    while n < times:
        print("Add number no", n+1)
        number = float(input())
        somme = somme + number
        n = n + 1
    print("The somme of the", n, "numbers that you added is:", somme) 