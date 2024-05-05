#Type Function And Data Types in Python 

print("Type of 4 :", type (4))
print("Type of 4.0  :",type(4.0))
print("Type of '4' :",type('4'))
print("Type of 'A' :",type('A'))
print("Type of \"ABC\":",type("ABC"))
print("Type of 4j :",type(4j))

#Representing Integers

# decimal literal
x = 100
print("Type of" , x , " : ",type(x) )

# x = 0144 (SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers )


# decimal literal
x = 100

#octal Integer Literal
x = 0o144
print ("type of", x ," : " , type (x))


#HexaDecimal Integer Literal
x = 0x64
print("type of ", x , " : ",type(x))


#Binary Integer Literal
x = 0b1100100
print("type of ", x , " : ",type(x))


result = 100 + 0o144 + 0x64 + 0b1100100
print("Result ;",result)
