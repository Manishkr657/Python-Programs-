#first we will get inputes from users 
a= float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))

#using lambda functions for calculations
x= lambda a,b: (a*b) 
y= lambda a,b: (pow(a,2)+ (a+b)*2 + pow(b,2))

#printing values after solution 
print(x(a,b))
print(y(a,b))