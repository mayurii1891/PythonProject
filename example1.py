Weight=int(input("Enter your weight:"))
Height=float(input("Enter your height:"))
BMI=Weight/(Height*Height)
print("BMI is:",BMI)
if BMI< 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <=24.9:
    print("Normal weight")
elif BMI>=25 and BMI<=29.9:
    print("Overweight")
elif BMI>30:
    print("Obese")
