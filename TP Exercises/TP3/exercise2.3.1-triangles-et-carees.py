from turtle import *
shape('turtle')
a = 1
b=1
c = 1
y = 200
d = 1
reset()
up()
speed(10)
goto(-200, 200)
while c < 5:
    while b < 5:
        while a < 5:
            down()
            right(90)
            forward(50)
            up()
            a = a + 1
        forward(10)
        while d < 4:
            down()
            forward(50)
            right(120)
            d = d + 1
            up()
        forward(110)
        a = 1 
        d = 1
        b = b +1
    forward(110)
    
    goto(-200, y-60)
    b = 1
    y = y -60
    c = c + 1