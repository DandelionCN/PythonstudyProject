# 3.1 数字的四舍五入

print( round(1.23456,4))

print(round(1.5,0))
print(round(2.5,0))


a=124658694385
print(a)
print(round(a,-1))
print(round(a,-2))
print(round(a,-5))

x=1.23456
print(format(x,'0.3f'))
print('Value is {:0.3f}'.format(x))


#高精度的浮点数运算Decimal(notcie the Capital Letter)
from decimal import Decimal
a=Decimal('365000')
b=Decimal('12')
print('a/b=',a/b)
print('a/b={:0.3f}'.format(a/b))
print('a/b={:0,.3f}'.format(a/b))
print('a/b={:0.3e}'.format(a/b))





