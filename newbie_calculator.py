#a newbie calculator
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
#in python we need to do typecasting for integer type input since the default is string 
sum= int(num1) + int(num2)
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))
difference = int(num1) - int(num2)
print("The difference of {0} and {1} is {2}".format(num1, num2, difference))
product = int(num1) * int(num2)
print("The product of {0} and {1} is {2}".format(num1, num2, product))
division = float(num1) / float(num2)
print("The division of {0} by {1} is {2}".format(num1, num2, division))
remainder = float(num1) % float(num2)
print("The remainder of {0} on dividing by {1} is {2}".format(num1, num2, remainder))
