number_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_list = list(set(number_list))

print("List after removing duplicates:", unique_list)