def triangle():
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    area = (base * height) / 2
    return area
result = triangle()
print(f"The area of the triangle is {result}")