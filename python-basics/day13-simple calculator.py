num1=int(input("Enter Number1 : "))
num2=int(input("Enter Number2 : "))
Operator=input("Enter Operetor : ")
if Operator == '+':
    print(num1 + num2)
elif Operator == '-':
    print(num1 - num2)
elif Operator == '*':
    print(num1 * num2)
elif Operator == '/':
    if num2 == 0 :
        print("Division by zero!")
    else :
       print(num1 / num2)
else :
    print("Error")
    
