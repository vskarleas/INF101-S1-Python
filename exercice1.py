>>> 3+5
8
>>> "bon"+"jour"
'bonjour'
>>> "3"+"5"
'35'
>>> 3+"5"
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    3+"5"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 3+ "5"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    3+ "5"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 3+int("5")
8
>>> 1/1
1.0
>>> 1+1
2
>>> "1"+"1"
'11'
>>> a=3
>>> print(a)
3
>>> type(a)
<class 'int'>
>>> a=a+17
>>> b=a*2
>>> print("a=",a,"b=",b)
a= 20 b= 40
>>> a==b
False
>>> type(a==b)
<class 'bool'>
>>> type(a=b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    type(a=b)
TypeError: type() takes 1 or 3 arguments
>>> 17//5
3
>>> 17/5
3.4
>>> 17%5
2
>>> 17.0/5
3.4
>>> type(3.3)
<class 'float'>
>>> 
