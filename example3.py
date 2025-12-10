import datetime
name=str(input("enter name: "))
print("hii!",name,"welcome to BMI & Diet Planner" )
date=int(input("Enter your birth date:"))
month=int(input("Enter your birth month:"))
year=int(input("Enter your birth year:"))
day=datetime.date(year,month,date)
Day= f"{day:%A}"
print("Awesome!",name," You were born on a", Day)
print("To calculate BMI, please enter the required details.")
Weight=int(input("Enter your weight:"))
Height=float(input("Enter your height:"))

BMI=Weight/(Height*Height)
print("According to your height and weight, your BMI is=",BMI)
if BMI< 18.5:
    print("Your BMI is below 18.5, which means you fall into the Underweight category.")
    print("Would you like me to suggest a healthier diet plan for you?")
    user_choice = str(input("yes/no:"))
    if user_choice == "yes":
        print("Diet Plan to Reach Normal Weight:")
        print("1. Eat 5–6 small meals a day.")
        print("2. Add calorie-dense foods like nuts, seeds, and dried fruits.")
        print("3. Include protein-rich foods (milk, eggs, beans, paneer).")
        print("4. Have healthy carbs (rice, whole wheat, potatoes, oats).")
        print("5. Use healthy fats like olive oil, avocado, and nuts.")
        print("6. Drink smoothies or milkshakes for extra calories.")
        print("7. Do light exercise to build muscle mass.")
    else:
        print("No problem! Stay healthy and have a wonderful day")
elif BMI >= 18.5 and BMI <=24.9:
    print("Great job! Your BMI is in the Normal range, which means you have a healthy weight for your height.")
elif BMI>=25 and BMI<=29.9:
    print("Your BMI is in the Overweight range, which means you have more weight than is considered healthy for your height.")
    print("Would you like me to suggest a healthier diet plan for you?")
    user_choice = str(input("yes/no:"))
    if user_choice == "yes":
        print(" Diet Plan to Reach Normal Weight:")
        print("1. Control portion sizes and reduce excess calories.")
        print("2. Eat more fruits, vegetables, and fiber-rich foods.")
        print("3. Replace refined carbs with whole grains (brown rice, oats, wheat).")
        print("4. Add lean proteins (fish, chicken, pulses, eggs).")
        print("5. Use healthy fats like olive oil, nuts, and seeds.")
        print("6. Avoid fried/junk food and sugary drinks.")
        print("7. Stay hydrated with 2–3 liters of water daily.")
        print("8. Exercise at least 30 minutes a day (walking, jogging, yoga).")
    else:
        print("No problem! Stay healthy and have a wonderful day")
elif BMI>=30:
    print("Your BMI shows that you are in the Obese category. A healthier diet and lifestyle changes can help you move toward the Normal range.")
    print("Would you like me to suggest a healthier diet plan for you?")
    user_choice = str(input("yes/no:"))
    if user_choice == "yes":
        print("Diet & Lifestyle Plan to Reach Normal Weight:")
        print("1. Create a calorie deficit — eat fewer calories than you burn.")
        print("2. Eat more fruits, vegetables, and high-fiber foods.")
        print("3. Replace refined carbs with whole grains (brown rice, oats, wheat).")
        print("4. Add lean proteins like chicken, fish, legumes, and eggs.")
        print("5. Avoid fried foods, sweets, sugary drinks, and junk food.")
        print("6. Stay hydrated (3–4 liters of water daily).")
        print("7. Exercise at least 40–60 minutes a day (walking, jogging, or gym).")
        print("8. Sleep 7–8 hours daily to support weight management.")
    else:
        print("No problem! Stay healthy and have a wonderful day")