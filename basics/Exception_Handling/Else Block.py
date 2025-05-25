def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        print("Division successful, no exceptions occurred.")

divide(20,5)
print(f"Division result: {divide(20, 5)}")  # Output: Division result: 4.0////MILE NAI