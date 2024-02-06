number = int(input("Enter the no."))
print("The Multipication Table of:",number)
sum = 0
for count in range(1,11):
    print(number, 'x' , count, '=' , number*count)
    sum = sum + number * count
print(sum)

