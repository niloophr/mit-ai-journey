n1 = int(input("Enter Number1 : "))
n2 = int(input("Enter Number2 : "))
n3 = int(input("Enter Number3 : "))

if n1 >= n2 and n1 >= n3:
    print(f'{n1} is the biggest number')
elif n2 >= n1 and n2 >= n3:
    print(f'{n2} is the biggest number')
else:
    print(f'{n3} is the biggest number')
