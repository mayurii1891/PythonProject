angle1=int(input("Enter 1st angle1:"))
angle2=int(input("Enter 2nd angle2:"))
angle3=int(input("Enter 3rd angle3:"))
if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
    print("yes,tringle can be formed")
else:
    print("No,tringle cannot be formed")