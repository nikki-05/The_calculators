
#This is the most basic calculator we are going to create 
print("----C A L C U L A T O R----")
# This function adds two numbers
def add(a, b):
    return a+b

# This function subtracts two numbers
def subtract(a, b):
    return a-b

# This function multiplies two numbers
def multiply(a, b):
    return a*b

# This function divides two numbers
def divide(a, b):
    return a/b


print("Select operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divition")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the  first number: "))
            num2 = float(input("Enter  the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # break the while loop if answer is no
        print("want to continue ?")
        next_cal = input("Let's do next calculation? (yes/no): ")
        if next_cal== "no":
          print("that's okey!")
          break
    else:
        print("Invalid Input try again")