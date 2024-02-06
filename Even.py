n=int(input("start no.:-"))
m=int(input("end no.:-"))
if(n<m):
    while(n<=m):
        if(n%2==0):
            print(n)
            n=n+2
        else:
            n=n+1
else:
    while(n>=m):
        if(n%2==0):
            print(n)
            n=n-2
        else:
            n=n-1