height_cm=float(input("Enter Your height : "))
weight_kg=float(input("Enter Your weight : "))

height_m= height_cm/100
BMI=weight_kg/(height_m*height_m)

if BMI <18.5 :
    print(f"BMI :{BMI:.2F} ")
    print("State : Underweight")
    print("Recommendation : Eat more, but wisely. See a doctor first.")
elif 18.5 <= BMI < 25 :
    print(f"BMI :{BMI:.2F} ")
    print("State : Normal")
    print("Recommendation : Maintain your weight with a balanced diet and regular exercise.")
elif 25 <= BMI < 30 :
    print(f"BMI :{BMI:.2F} ")
    print("State : Overweight")
    print("Recommendation : Eat less, move more, and focus on whole foods.")
else :
    print(f"BMI :{BMI:.2F} ")
    print("State : Obese")
    print("Recommendation : Have excess body weight.")


