list1 = ["python", "java", "c++", "javascript", "ruby", "swift"]
actual_list = list.copy(list1 )
print("Original List:", actual_list)

testList = list(actual_list)
print("Copied List:", testList)

slice_list = actual_list[1:4]
print("Sliced List:", slice_list)


list1 = ["python", "java", "c++"]
list2 = ["javascript", "ruby", "swift"]
# Using + operator
list3 = list1 + list2
print("List after joining using + operator:", list3)

for x in list2:
    list1.append(x)
print("List after joining using append() method:", list1)