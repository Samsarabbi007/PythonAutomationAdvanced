list = ["python", "java", "c++", "javascript", "ruby", "swift"]

for x in list:
    print(x)

for x in range(len(list)):
    print(list[x])

for i in range(len(list)):
    print(f"Index:{i} Value:{list[i]}")


[print(f"Index:{i} Value:{list[i]}") for i in range(len(list))]