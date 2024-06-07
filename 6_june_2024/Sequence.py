# Build Program Using Sequence Construct 
#program for Calculation Addition of Two integer 
number1 = int(input("Please Enter The First  Integer : "))
number2 = int(input("Please Enter The Second Integer : "))
addition = number1 + number2 
print(number1 ,"+",number2,"=",addition)

# Given The Radius of a Circle Find The Area and Circumference
radius = float(input("Please Enter The Radius Of The Circle in cm : "))
area_circle = 3.14 *(radius*radius)
Circumference = 2*3.14*radius
print("Area Of Circle With Radius ",radius,"is",area_circle)
print("Circumference Of Circle With Radius ",radius,"is",Circumference)

#In this we will round off the precision
radius = float(input("please enter the radius of the circle in cm :"))
area_circle = 3.14 * (radius * radius)
circumference = 2*3.14*radius
#Using Character Map (Keystroke)
print("Area of circle with radius ",radius,"is" ,round(area_circle,2),"cm²" )
print("Circumference of circle with radius ",radius,"is",round(circumference,2),"cm")

#Using Character map
print("Alt+0178 :² ")
print("Alt+0190 :¾")

#Unicode
symbol ='\u00b2'
print("Symbol :",symbol)
symbol = '\u00BE'
print("Symbol =",symbol)

#In this we will round off the precision
import math
radius = float(input("please enter the radius of the circle in cm :"))
area_circle = math.pi * (radius * radius)
circumference = 2*math.pi*radius
print("Area of circle with radius ",radius,"is" ,round(area_circle,2),"cm²" )
print("Circumference of circle with radius ",radius,"is",round(circumference,2),"cm")

