set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}

# Union of two sets
set_union = set_1.union(set_2)
print(f"Union of set_1 and set_2: {set_union}")  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection of two sets
set_intersection = set_1.intersection(set_2)
print(f"Intersection of set_1 and set_2: {set_intersection}")  # Output: {4, 5}
# Difference of two sets
set_difference = set_1.difference(set_2)
print(f"Difference of set_1 and set_2: {set_difference}")  # Output: {1, 2, 3}
# Symmetric difference of two sets
set_symmetric_difference = set_1.symmetric_difference(set_2)
print(f"Symmetric difference of set_1 and set_2: {set_symmetric_difference}")  # Output: {1, 2, 3, 6, 7, 8}

#Copy a set
set_copy = set_1.copy()
print(f"Copied set_1: {set_copy}")  # Output: {1, 2, 3, 4, 5}