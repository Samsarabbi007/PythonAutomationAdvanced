age = 18
if age>= 18:
    print("You are an adult")
else:
    print("You are not an adult")


'''number1 = 10
number2 = 10
if number1 > number2:
    print("Both numbers are equal")
    print(f"{number1} is greater than {number2}")
elif number1 < number2:
    print(f"{number1} is less than {number2}")
else:
   print("Both numbers are equal")
'''
# Nested if else
age = 20
citizenship = "BD"
if age >= 18:
    if citizenship == "BD":
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote due to citizenship")
else:
    print("You are not eligible to vote due to age")

age = 20
citizenship = "BD"
area = "Dhaka"
if age >= 18:
    if citizenship == "BD":
        if area == "Dhaka":
            print("You are eligible to vote in Dhaka")
        else:
            print("You are not eligible to vote due to area")
    else:
        print("You are not eligible to vote due to citizenship")
else:
        print("You are not eligible to vote due to age")

