def find_intersection(list1, list2):
    return list(set(list1) & set(list2))

# Input from user
list1 = input("Enter elements of first list (space-separated): ").split()
list2 = input("Enter elements of second list (space-separated): ").split()

intersection = find_intersection(list1, list2)
print("Intersection of the two lists is:", intersection)

def find_union(list1, list2):
    return list(set(list1) | set(list2))

# Input from user
list1 = input("Enter elements of first list (space-separated): ").split()
list2 = input("Enter elements of second list (space-separated): ").split()

union = find_union(list1, list2)
print("Union of the two lists is:", union)