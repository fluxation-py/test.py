expression=input("Enter an expression, (+) (-) (*) (/): ")
num1=float(input("Enter a number: "))
num2=float(input("Enter another number:"))

if expression=="+":
    print(num1+num2)

elif expression=="-":
    print(num1-num2)

elif expression=="*":
    print(num1*num2)

elif expression=="/":
    print(num1/num2)


else:
    print("Please enter a valid expression.")
