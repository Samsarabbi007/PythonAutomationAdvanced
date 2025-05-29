number_list = (list(map(int, input("Enter numbers separated by spaces: ").split())))
sorted_list = sorted(number_list)

print("Sorted list (ascending):", sorted_list)


number_list = (list(map(int, input("Enter numbers separated by spaces: ").split())))
sorted_list1 = sorted(number_list,reverse=True)

print("Sorted list (descending):", sorted_list1)