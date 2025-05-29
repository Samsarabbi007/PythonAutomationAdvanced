numbers = [10, 25, 4, 99, 67, 88]
print("The smallest number is:", min(numbers))


def find_smallest(nums):
    if len(nums) == 0:
        return None
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest

# User input
input_str = input("Enter numbers separated by spaces: ")
number_list = list(map(int, input_str.split()))

# Find and display result
smallest = find_smallest(number_list)
print("The smallest number is:", smallest)