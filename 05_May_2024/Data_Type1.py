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

# 34 + 'Anil'TypeError: unsupported operand type(s) for +: 'int' and 'str'

name = input("What's your name ? ")
age =  input("How old are you? ")
print("hello",name,  "you are",age, "Years old")
# TypeError: can only concatenate str (not "int") to str
#print("but you will be", age + 2,"years old two years later")

#Converting a String into integer
age = input("How old are you ?")
print("Type of age ",type(age))

#Correction 
name = input("What's your name ? ")
age =int(  input("How old are you? "))
print("hello",name,  "you are",age, "Years old")
print("but you will be", age + 2,"years old two years later")
#Output
      #----> 2 age =int(  input("How old are you? "))
      # ValueError: invalid literal for int() with base 10: 'oxf'
print(int(100))
#print(int('ox64'))
#ValueError: invalid literal for int() with base 10: 'ox64'
#print(int('0b1100100'))
#ValueError: invalid literal for int() with base 10: '0b1100100'

#    ************** Converts a string representing integer in decimal format to integer ************
print(int('100', base = 10))
# ->100
#Converts a string representing integer in  Hexadecimal format to integer
print(int('0x64', base = 16))
# ->100
#Converts a string representing integer in Binary  format to integer
print(int('0b1100100', base = 2))
# ->100
#Converts a string representing integer in Octal  format to integer
print(int('0o144', base = 8))
# ->100

