lst = list(map(float, input("Enter numbers separated by spaces: ").split()))  # List input

if len(lst) < 2:
    print("List mutst have at least 2 elements")
else:
    lst.sort()
    print(f"The second largest element is: {lst[-2]}")