def add(a=0,b=0):
    return a+b
result = add(100,644)
print(result)


def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print("Find Max number:",find_max([10,2,30,4,55]))
print("Find Max number:",find_max([10,2,30,4,559,5]))