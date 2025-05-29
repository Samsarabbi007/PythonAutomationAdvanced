def multiply_list(nums):
    result = 1
    for num in nums:
        result *= num
    return result

# Get input from user
input_str = input("Enter numbers separated by spaces: ")
number_list = list(map(int, input_str.split()))

# Calculate product
Total = multiply_list(number_list)

print("Product of all elements in the list is:", Total)