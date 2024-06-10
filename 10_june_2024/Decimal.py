#module decimal
#Module Names are in SmallCase & Class and Type are in Uppercase eg: Decimal

n1 = 0.1 + 0.1 + 0.1 
n2 = 0.3
print(n1==n2)
print((0.1+0.1+0.1)==(0.3))
print(type(n1),type(n2))

n1 = 0.1 + 0.1 + 0.1
print("n1 :",n1)
print("n1 :",round(n1,3))

#0.001
#0/2 + 0/4 +1/8 
0.1 + 0.1 + 0.1 - 0.3
1.1 + 2.2

import decimal
print(dir(decimal))
#important Concepts  in decimal module are 'ROUND_05UP', 'ROUND_CEILING', 'ROUND_DOWN', 'ROUND_FLOOR',
#'ROUND_HALF_DOWN', 'ROUND_HALF_EVEN', 'ROUND_HALF_UP', 'ROUND_UP', 'Rounded', 'Subnormal', 'Context'
#,'getcontext', 'localcontext', 'setcontext'

from decimal import Decimal
x = Decimal(4) # int as a argument 
print("Decimal Value :",x)
print("Type of x :",type(x))

x = Decimal('4') # string as a argument 
print("Decimal Value :",x)
print("Type of x :",type(x))
