number_list=[10, 4, 3, 50, 23, 90]
def find_largest_three_numbers(number_list):
   sorted_List = sorted(number_list)
   #print(list(reversed(sorted_List)))
   largest_three_numbers =list(reversed(sorted_List[3:]))
   return largest_three_numbers

print(find_largest_three_numbers(number_list))

