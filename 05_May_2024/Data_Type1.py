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


num = 32
print("num = ", num)
num = 0b100000
print("num = ", num)

#Converting Integer

num = 2000
print(num,"in hexadecimal format :",hex(num))
print(num, " in octal format :", oct(num))
print(num, "in binary format : " , bin(num))

#The Function hex, bin , Oct Can be used to convert an integer Number into corresponding String Representation

Result = hex(2000) + oct(2000) + bin(2000)
print("Result :", Result )

34' + '4'
