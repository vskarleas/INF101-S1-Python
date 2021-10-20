#1
def fibonacci(n):
    a = 0
    b = 1
    if n > 0:
        for n in range(1, n):
            c = a + b
            a = b
            b = c
            print(c)
    elif n == 0 or n == 1:
        print("The fibonacci number is", b)

#2
def fibonacci_2(n):
    a = 0
    b = 1
    if n > 0:
        for n in range(1, n):
            c = a + b
            a = b
            b = c
    elif n == 0 or n == 1:
        print("The fibonacci number is", b)
    return c

#3
def nombre_or(n):
    a = 0
    b = 1
    listing=[]
    if n > 0:
        for n in range(1, n):
            c = a + b
            a = b
            b = c
            listing.append(c)
            fn = c
        o = len(listing)
        new_list = listing[o-2:o-1:1]
        fn1= new_list[0]
        result = fn/fn1
        return result #maybe this gives the solution in question 4 as well 

n = 5797
print(nombre_or(n))