number_list=[10, 4, 3, 50, 23, 90]
def find_largest_three_numbers(number_list):
   sorted_List = sorted(number_list)
   #print(list(reversed(sorted_List)))
   largest_three_numbers =list(reversed(sorted_List[3:]))
   return largest_three_numbers

print(find_largest_three_numbers(number_list))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = max(num1, num2, num3)
print("The largest number is:", largest)