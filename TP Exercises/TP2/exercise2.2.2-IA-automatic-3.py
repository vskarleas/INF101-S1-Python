import random
print("IA aleartoire")
n = int(input("How many times to play ?"))
mql = int(input("How many times to try in a single play ?"))
if 0 < n < 10**300:
    win=0
    lose=0
    restart = 1
    while 0 < restart <= n:
        x = random.randint(0,100)
        print("I choose", x)
        print("----------")
        g = 1
        k = 0
        r = 100
        print("I search a number between 0 and 100")
        a = random.randint(0, 100)
        z=0
        print("I propose", a)
        while 0 < g < mql:
            if a > x:
                print("I search a number between",k," and ", a-1)
                r=a-1
                a = random.randint(k, a-1)
                print("I propose", a)
                if a > k:
                    k = k
                else: 
                    k = a
        
                g = g + 1
                
            elif a < x:
                z=a
                k=z
                print("I search a number between",z+1," and ", r)
                a = random.randint(z+1, r)
                print("I propose", a)
                if a < r:
                    r = r
                else: 
                    r = a
        
                g = g + 1
                
            elif a == x:
                print("I won")
                g = 10000
                
        if g == 10000:
            print("It found the correct number")
            win = win + 1
            restart = restart + 1
        if g < n:
            print("It runned out of times.",mql,"times is maximum tries for a single play")
            lose = lose + 1
            restart = restart + 1
    print("It tried in total", n, "as you told in the beginning of the programm. When the program can't define a correct answer, it continues to try with the maximum amount of tries that remains until the tries are finished or it finds the number so that  it can restart the process and search for the new defined number from the IA. If it's runned out of times, it can't continue to this step.")
    print("We can define how many times we want the AI to try to find a number and the number of plays seperatly. This is why there is also the variable mql with an input. It defines the number of tries inside a single game.")
    lose = n - win
    print("It found the number", win,"times and it lost", lose, "times")
    print("The average of failed tries was sur pourcentage is ", (lose/n)*100,"%")