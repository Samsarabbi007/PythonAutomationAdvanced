my_Set = {1, 2, "username", "password", 3.14,5}
#remove an item from the set
my_Set.remove("username")  # Removes the item "username")
print(f"Set after removing 'username': {my_Set}")

my_Set.discard(3.14)  # Removes the item 3.14, if it exists
print(f"Set after discarding 3.14: {my_Set}")

#using pop to remove an arbitrary item
my_Set.pop()
print(f"Set after removing from set: {my_Set}")

# using clear to remove all items from the set
my_Set.clear()  # Removes all items from the set
print(f"Set after clearing all items: {my_Set}")