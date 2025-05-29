s=input("Enter a string to reversed: ")

rev1=s[::-1]
print(f"The reversed string is {rev1}")


rev2="".join(reversed(s))
print(f"The reversed string is {rev2}")


rev3=""
for x in reversed(s):
    rev3+=x
print(f"The reversed string is {rev3}")

