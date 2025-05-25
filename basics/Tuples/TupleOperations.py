#Copy
OriginalTuple = (1, 2, 3,4,5,6,71,41,7,8,9,10,12)
OriginalTuple2 = (11, 12, 13, 14, 15)
copied_tuple = OriginalTuple
print(f"Original Tuple: {OriginalTuple}")
#sorting a tuple
sorted_tuple = (sorted(OriginalTuple))
print(f"Sorted Tuple: {sorted_tuple}")
# Reversing a tuple
reversed_tuple = OriginalTuple[::-1]
print(f"Reversed Tuple: {reversed_tuple}")

# joining tuples
joined_tuple = OriginalTuple + OriginalTuple
print(f"Joined Tuple: {joined_tuple}")

# Nesting tuples
nested_tuple = (OriginalTuple, OriginalTuple2)
print(f"Nested Tuple: {nested_tuple}")
nested_tuple2 = ((1,3,5), (2,4,6))
print(f"Nested Tuple 2: {nested_tuple2}")

print(f"nested Tuple 2[1][2]: {nested_tuple2[1][2]}")  # Accessing an element in a nested tuple
