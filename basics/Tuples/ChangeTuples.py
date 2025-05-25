# Tuples are immutable, meaning they cannot be changed after creation.
my_tuple = (1, 2, "username", "password", 3.14, True)
# Attempting to change an element will raise an error
new_Tuple = my_tuple[:2] + ("new_value",) + my_tuple[3:]
print("New Tuple:", new_Tuple)  # Output: (1, 2, 'new_value', 'password', 3.14, True)
# Attempting to change an element will raise an error
# my_tuple[0] = 10  # This will raise a TypeError
# Attempting to change an element will raise a TypeError
# print("Modified Tuple:", my_tuple)  # This line will not execute due to the error

del my_tuple
# The tuple is deleted, and any further access will raise an error
print(f" Deleted tuple",my_tuple)  # This will raise a NameError since my_tuple is deleted