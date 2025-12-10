import random
print(1)
name="Mayuri"
NAME=str(input("Enter your name:"))
if name==NAME:
    print("Name is:",NAME)
    print("Welcome",name,"to SBI Bank")
    Pin=1891
    PIN=int(input("Enter your PIN:"))
    if PIN == Pin:
        Otp=random.randint(1000,9999)
        print("OTP is:",Otp)
        OTP=int(input("Enter your OTP:"))
        if OTP == Otp:
            Amount=int(input("Enter Amount to withdraw:"))
            current_Amount=10000
            new_Amount=current_Amount-Amount
            if Amount > current_Amount:
                print("Insufficient Amount")
            else:
                print("Collect your cash.")
                print("New Balance is:",new_Amount)
        else:
            print("Incorrect OTP")
    else:
        print("Invalid PIN!")
else:
    print("Invalid User!")
