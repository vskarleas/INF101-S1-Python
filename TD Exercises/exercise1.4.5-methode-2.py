def sum_digits(n):
    s = 0
    if n < 0:
        n = ((-1) * n)
    while n>0:
        s += n % 10
        n //= 10 #floor division. Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
    print(s)

n = int(input("Entier:"))
sum_digits(n)