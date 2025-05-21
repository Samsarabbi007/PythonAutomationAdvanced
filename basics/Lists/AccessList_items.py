list1 = ["Python", "Java", "C++", "JavaScript"]
#indexing
print(list1[2])  # Output: C++
#negative indexing
print(list1[-1])  # Output: JavaScript
print(list1[-2])  # Output: C++
#slicing
print(list1[1:3])  # Output: ['Java', 'C++']// list [start:end-1]
print(list1[1:])  # Output: ['Java', 'C++', 'JavaScript']
print(list1[:3])  # Output: ['Python', 'Java', 'C++']
print(list1[::2])  # Output: ['Python', 'C++']
print(list1[::-1])  # Output: ['JavaScript', 'C++', 'Java', 'Python']//buji nai
print(list1[::-2])  # Output: ['JavaScript', 'Java']

if "Python" in list1:
    print("Python is in the list")
else:
    print("Python is not in the list")

