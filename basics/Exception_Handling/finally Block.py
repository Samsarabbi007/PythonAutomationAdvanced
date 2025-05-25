def divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        print("Cannot divide by zero")

    finally:
        print("Execution of the divide function is complete.")

divide(20,0)