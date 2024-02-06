#creating functions for performing calculation....
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def div(x,y):
    return x/y

#putting values for calculations 
print("*Select choice*")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#now putting conditions for calculation
while True:
    #asking for choices for calculations
    choice = input("Enter choices (1/ 2/ 3/ 4):")
    
    #choice 
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
         
    
    

    