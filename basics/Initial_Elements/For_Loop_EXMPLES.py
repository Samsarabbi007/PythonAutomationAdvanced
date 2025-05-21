'''
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

for x in fruits:
    print(x)

# for i in range(5):
for x in range(15):
    print(x)
#for i in range(start, stop, step):
# for i in range(1, 10):
for x in range(5, 10):
    print(x)
# for i in range(1, 10, 2):
for x in range(1, 10, 2):
    print(x)

for x in range(1, 10, 2):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

colors = ["red", "green", "blue"]
fruits = ["apple", "banana", "orange"]
for x in colors:
    for y in fruits:
        print(x, y)

fruits = ["apple", "banana", "test"]
actual_fruits = []
for x in fruits:
    if x == "test":
        continue
    print(x)
    actual_fruits.append(x)

print(actual_fruits)
'''
Fruits = ["apple", "banana", "orange"]
for fruit in Fruits:
    print(fruit)
    if fruit == "banana":
        break