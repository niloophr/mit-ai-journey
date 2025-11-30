user=str(input("Enter Username : "))
password=int(input("Enter pessword : "))

correctusername="admin"
correctpassword=1234

if user==correctusername and password==correctpassword :
    print(f"wellcome user {user}")
elif user==correctusername and password!=correctpassword :
    print(f"user {user} , your password incorrect , please enter correct password")
elif user!=correctusername and password==correctpassword :
    print(f"user {user} , your username incorrect , please enter correct username")
else :
    print("Both username and password incorrect , try again !")
