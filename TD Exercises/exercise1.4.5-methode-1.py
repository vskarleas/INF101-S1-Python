
def function(x):
    sum_of_digits = 0
    for digit in str(x):
        sum_of_digits += int(digit) #the same by writing sum_of_digits = sum_of_digits + int(digit)

    print(sum_of_digits)

x = int(input("Entier:"))
function(x)