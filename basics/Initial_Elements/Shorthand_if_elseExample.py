x= int(input("Enter a number: "))
#print("Positive" if x>0 else "Negative")

#Nested Shorthand if else
#result ="positive" if x>0 else "Even" if x%2==0 else"ODD" if x<0 else "zero"
#result = "Positive" if x>0 else "Negative" if x<0 else "Zero"

result = "Large" if x>10 else "Small" if x<5 else "Midium"
print(result)
