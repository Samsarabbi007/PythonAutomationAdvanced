#and
from operator import truediv

x = True
y = False
print(x and y)

a=20
b=30
print(a>15 and b<30)

#OR
x = True
y = False
print(x or y)

a=20
b=30
print(a>25 or b<30)
#not
x= True
print(not (x))

#case1 age>=18 and has_ticket=True
#case2 adult and has_ticket=True
age = 20
has_ticket = True
is_adult = True

if(age>=22 and has_ticket) or (is_adult and has_ticket):
    print("You can watch the movie")



