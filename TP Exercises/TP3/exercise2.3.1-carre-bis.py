from turtle import *
reset()
speed(1)
shape('turtle')
a = 1
up()
goto(-50,20)
down()
while a < 5:
    down()
    forward(100)
    right(90)
    a = a + 1