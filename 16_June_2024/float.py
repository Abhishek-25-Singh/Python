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

