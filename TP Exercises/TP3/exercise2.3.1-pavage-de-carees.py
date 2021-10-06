from turtle import *
shape('turtle')
a = 1
b=1
c = 1
y = 200
reset()
up()
speed(100)
goto(-200, 200)
while c < 5:
    while b < 9:
        while a < 5:
            down()
            right(90)
            forward(50)
            up()
            a = a + 1
        a = 1 
        forward(60)
        b = b +1
    goto(-200, y-60)
    b = 1
    y = y -60
    c = c + 1