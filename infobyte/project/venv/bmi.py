weight = float(input("Enter your weight in kg "))
height = float(input("Enter your height in CentiMeters "))

height_in_meters = height / 100

BMI = weight / (height_in_meters**2)
print(BMI)

if (BMI<16):
    print("you are sevraly underweight")

elif (BMI >= 16 and BMI < 18.5):
    print("you are underweight")
    
elif (BMI >= 18.5 and BMI < 24):
    print("You are Healthy") 

elif (BMI >= 24 and BMI < 30):
    print("you r Overweight")

elif (BMI >= 30):
    print("You are Stupid")

