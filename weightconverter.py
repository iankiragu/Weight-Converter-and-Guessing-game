weight = input("Kindly enter your weight here = ")
unit = input('(K)gs or (L)bs = ')
if unit.upper() == "K":
    lbs = int(weight) * 2.20462
    print("Your weight in pounds is = " + str(lbs))
elif unit.upper() == "L":
    kgs = int(weight) * 0.45
    print("Your weight in kgs is = " + str(kgs))