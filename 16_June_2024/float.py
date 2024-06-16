#int rollNo;
#float Perc;


#Checking type of the variable
rollNo = 5
perc = 77.78
print("Type of Roll No    : ", type(rollNo))
print("Type of percentage : ", type(perc))
#Checking Type of Values 
print("Type of 5 :",type(5))
print("Type of 5.5 :",type(5.5))


rollNO = 5
perc = 77.78
print("Is roll NO is integer Type :",isinstance(rollNO,int))
print("Is percentage is Integer Type :",isinstance(perc,int))
print("Is Percentage is Float type :",isinstance(perc,float))
print("Is 445 is a Numeric type :",isinstance(445,(int,float)))
print("Is 44.5 is a Numeric type :",isinstance(44.5,(int,float)))

#as_integer_ratio():
#Return a pair of integers whose ratio is exactly equal to the original float.
#and with a positive denominator 
from math import pi
print("PI :",pi)
 #(Name_Of_The_Variable.as_integer_ratio(numerator, denominator))
print("PI as a Fraction :", pi.as_integer_ratio())

x= 0.125
print("X as a Fraction :",x.as_integer_ratio())
x= 21
print("X as a Fraction :",x.as_integer_ratio())
x= 0
print("X as a Fraction :",x.as_integer_ratio())


# Floating point in Hexadecimal point
x = 0.125
print("x =",x)
hexrep = x.hex()
print("x in hex =",hexrep)
print("Type of hexrep = ", type(hexrep))
x = float(hexrep,16)
print("x =",x)

# Floating point in Hexadecimal point
x = 0.125
print("x =",x)
hexStr = x.hex()
print("x in hex =",hexStr)
print("Type of hexStr = ", type(hexStr))
x1 = float.fromhex(hexStr)
print("x1 =",x1)

s = '67.8'
float(s)


#Understanding Complex Number
x = 1.5 + 1.5j
print("Complex number = ",x)

x = 5 + 6j
print("Complex number = ",x)

x= complex()  #no arg
print("Complex number = ",x)

x= complex(4.5)  #one args
print("Complex number = ",x)

x= complex(4.5,1.5)  #TWO ARGS: real and imaginary
print("Complex number = ",x)

x = complex('3.5+1.5j')  # string as an argument
print("Complex number =", x)

x = input("Give me a Complex Number :")
print("The complex Number is",x,type(x))
x=x+(5+6j)
