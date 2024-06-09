#Exploring  The floating Point Data type :float
print("type of 4.5 :" , type(4.5))
print("Type of 45  : ", type(45))

#Repreenting Floating point in Exponential(Scientific) Format
x = 7.2
print("x = ",x,"type = " ,type(x))
x=700000000000000.0
print("x = ",x,"type = " ,type(x))
x=7.0E+14
print("x = ",x,"type = " ,type(x))
x=4.3E-3
print("x = ",x,"type = " ,type(x))
x=4.3E+3
print("x = ",x,"type = " ,type(x))


#isinstance(object, classinfo)
#Return True if the object argument is an instance of the classinfo argument,otherwise false
x = 7
print("Type of",x,":",type(x))
print("Is",x,"Of integer type ?",isinstance(x,int))
print("Is",x,"Of integer type ?",isinstance(x,float))

print()
x = 7.0
print("Type of",x,":",type(x))
print("Is",x,"Of integer type ?",isinstance(x,int))
print("Is",x,"Of integer type ?",isinstance(x,float))

print()
x = 7.0
print("Type of",x,":",type(x))
print("Is",x,"Of numeric type ?",isinstance(x,(int,float)))

print()

x = "Ketan"
print("Type of",x,":",type(x))
print("Is",x,"Of numeric type ?",isinstance(x,(int,float)))


#Maximum Vlue o Floating Point Number can have is approximately 1.8 x 10+308
x = 1.8E307  #Near The Maximum Value 
print("Maximum : " ,x)
x = 1.8E309  #Exceeds That Maximum Value 
print("Maximum : " ,x)

#The closest a non zero number can be to zero is approximately 5.0 X 10^-324
#Anything Closer to Zero than that is effectively zero
x = 5e-324
print("minimum :",x)
x=1e-325
print("mininmum :",x)

