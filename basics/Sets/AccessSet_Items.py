my_Set = {1, 2, "username", "password", 3.14, True}
# Accessing elements in a set
print(my_Set)
print("First element:", next(iter(my_Set)))  # Output: 1 or any other element, as sets are unordered

for item in my_Set:
    print("Item in set:", item)  # Output: Each item in the set, order may vary

