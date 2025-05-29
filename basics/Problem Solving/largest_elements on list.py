def find_largest_on_list(num1):
    if len(num1) == 0:
        return None
    largest = num1[0]
    for num in num1:
        if num > largest:
            largest = num
    return largest


input_str = input("Enter numbers separated by spaces: ")
number_list = list(map(int, input_str.split()))

largest = find_largest_on_list(number_list)
print("The largest number is:", largest)




lst = list(map(float, input("Enter numbers separated by spaces: ").split()))  # List input

# Check if list is empty
if not lst:
    print("The list is empty")
else:
    # Find the largest element
    largest = max(lst)
    print(f"The largest element is: {largest}")
