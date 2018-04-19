# 3.1 数字的四舍五入

print( round(1.23456,4))

print(round(1.5,0))
print(round(2.5,0))


a=124658694385
print(a)
print(round(a,-1))
print(round(a,-2))
print(round(a,-5))

x1=1.23456
print(format(x1,'0.3f'))
print('Value is {:0.3f}'.format(x1))


#高精度的浮点数运算Decimal(notcie the Capital Letter)
from decimal import Decimal
a=Decimal('365000')
b=Decimal('12')
print('a/b=',a/b)
print('a/b={:0.3f}'.format(a/b))
print('a/b={:0,.3f}'.format(a/b))
print('a/b={:0.3e}'.format(a/b))

#二八十六进制整数
x = 1234
print('X in bin format is:',bin(x))
print('X in oct format is:',oct(x))
print('X in hex format is:',hex(x))

print('X in bin format is :',format(x,'b'))
print('X in oct format is :',format(x,'o'))

print('X in hex format is:',int('11100010101010',2))

#分数运算Fraction（a,b）
from fractions import Fraction
a=Fraction(5,4)
b=Fraction(7,16)
print('a+b=',a+b)
print('a*b=',a*b)

