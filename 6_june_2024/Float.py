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
