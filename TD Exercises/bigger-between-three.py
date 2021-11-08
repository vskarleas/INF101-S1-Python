a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
maximum = 0

if a < b:
    if b < c:
        maximum = c #a<b<c
    else: #c<b
        maximum = b 

if b < c:
    if c < a:
        maximum = a
    else: #a<c
        maximum = c

if c < a:
    if a < b:
        maximum = b
    else: #b<a
        maximum = a

if a == b:
    if b < c:
        maximum = c
    else: 
        maximum = a #or b

if b == c:
    if c < a:
        maximum = a
    else: 
        maximum = b #or c

print("Maximum is ", maximum)