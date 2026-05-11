#Python Basic Calculator

print("Welcome to Python Basic Calculator! ")
num1= float(input("enter your number 1: "))
operator= input("select your operator, (+,-,*,/): ")
num2= float(input("enter your number 2: "))
if operator=="+":
    result=(num1+num2)
    print("Result =", result)
elif operator=="-":
    result=(num1-num2)
    print("Result =", result)
elif operator=="*":
    result=(num1*num2)
    print("Result =", result)
elif operator=="/":
    if num2!=0:
        result=(num1/num2)
        print("Result =", result)
    else:
         print("can't divide by zero")
else:
    print("invalid operator")
print("Thanks for using Python Calculator")