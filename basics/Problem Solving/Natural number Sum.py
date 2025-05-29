def sum_natural_numbers(n):
    if n < 1:
        return 0
    return n * (n + 1) // 2  # Using the formula

# Example usage
n = int(input("Enter a positive integer: "))
total = sum_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is {total}")