# --------Task1------
weight = 80  # weight = float(input("What is Your weight (kg)? : "))
height = 1.83  # height = float(input("What is Your height (m)? : "))
bmi = weight / (height ** 2)
lower_bound = 18.5
upper_bound = 25
result1 = bmi >= lower_bound and bmi <= upper_bound
result2 = "Your BMI is normal: True"
result3 = "Your BMI is normal: False"
result = int(result1) == 1 and str(result1) + result2 or int(result1) == 0 and str(result1) + result3
print(result)

# ------Task 2------
phone_number = input("Please, write here Your phone number:")
validnum = phone_number.isnumeric()
validlenght = len(phone_number) == 12
validstart = phone_number[:3] == "380"
valid = validnum and validlenght and validstart
print("Inputed number is valid: " + str(valid))
