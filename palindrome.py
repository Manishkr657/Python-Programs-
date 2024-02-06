num = input("Enter a value:") 
temp = num  
rev = 0  
while(num>0):  
    d = num % 10  
    rev = rev * 10 + d 
    num = num // 10  
if(temp == rev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  