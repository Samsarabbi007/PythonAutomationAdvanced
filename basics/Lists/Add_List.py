my_list = [1, 2, 3,"apple", "banana", "orange",4.5]
#Using Append
my_list.append("Orange")
my_list.append(True)
my_list.append(50)
print("List after appending:", my_list)

#Using Insert
my_list.insert(0,"Mango")
my_list.insert(2, "Grapes")
print("List after inserting:", my_list)

#Using Extend
my_list.extend(["Pineapple", "Watermelon"])
my_list.extend([True, 100])
print("List after extending:", my_list)