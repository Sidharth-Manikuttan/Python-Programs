import math
import cmath
num1=int(input('Enter the number : '))
num2=eval(input('Enter the number : '))
print("Square root of num1 is :",math.sqrt(num1))
print("Cube root of num1 is :",num1**(1/3))
s=cmath.sqrt(num2)
print('sqaure root of num2 is:',s.real,s.imag)
c=num2**(1/3)
print('cube root of num2 is:',c.real,c.imag)
