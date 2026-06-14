print("=== BMI Calculator ===")

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (meters): "))

if height <= 0:
    print("Invalid height")
else:
    bmi = weight / (height * height)

    print("\nYour BMI:", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")