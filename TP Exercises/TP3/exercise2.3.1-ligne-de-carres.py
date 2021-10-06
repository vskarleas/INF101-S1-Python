from turtle import *
shape('turtle')
a = 1
b=1
reset()
up()
goto(-200, 200)
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