x= int(input("enter the no. of rows for the pattern"))
for i in range(1,x):
    for j in range(1,i+1):
        print('*' , end="")
    print()