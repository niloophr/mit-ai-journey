score=float(input("Enter your Score : "))
if score>=0 and score<=20 :
    if score>= 18 and score<=20 :
      print("Your score is A ")
    elif score<=17 and score>=15 :
      print("Your score is B ")
    elif score<=14 and score>=12 :
      print("Your score is C ")
    elif score<=11 and score>=10 :
      print("Your score is D ")
    else :
      print("Your score is F")
else :
    print("score isn't on the range!!")
