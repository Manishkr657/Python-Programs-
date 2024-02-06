a=int(input("enter the number:"))
b=0
c=1
print(b)
print(c)
for x in range(a-2):
     temp=c
     c=b+c
     b=temp
     print(c)     
     
     
